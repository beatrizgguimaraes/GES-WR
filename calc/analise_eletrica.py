#!/usr/bin/env python3
"""Análise elétrica do exemplo de aplicação (robô do Time B, 2025).

Reproduz todos os números da seção de análise elétrica do capítulo 4 do TCC.
Cada constante indica a fonte. Nenhum valor ilustrativo entra no cálculo.
Execução: python3 analise_eletrica.py
"""
from math import log

# ---------------------------------------------------------------- bateria
C_AH = 5.2          # Ah  - TDP CBR 2025 (5200 mAh)
V_NOM = 11.1        # V   - TDP CBR 2025 (LiPo 3S, 11,1 V)
V_MIN = 9.0         # V   - descritivo 2025: tensão mínima de bateria (pré-requisito MainBoard)
C_RATE = 50         # C   - descritivo 2025 ("Bateria Leão Lipo 5200 mAh 3s 11.1 V 50 C")
E_NOM = C_AH * V_NOM  # Wh

# ---------------------------------------------------------------- tempo
T_REQ_MIN = 63.85   # min - tabela_estados_jogo_SSL v7, seção 7 (jogo longo)
T_REQ = T_REQ_MIN / 60.0  # h
T_EQUIPE = 60.0 / 60.0    # h - comunicação pessoal (gerente do projeto Lyra, 09/11/2026)
T_MEDIO = 39.57 / 60.0    # h - tabela v7, jogo médio ajustado

# frações do jogo longo (tabela v7, seção 6), denominador = t_req
FR = {"RUNNING": 0.2349, "HALT": 0.2438, "STOP": 0.2042,
      "BREAK": 0.1879, "TIMEOUT": 0.0957, "OUTROS": 0.0335}
D_MOTOR = {
    "conservador": 1.0,
    "central": FR["RUNNING"] + FR["STOP"] + FR["OUTROS"],   # 0,4726
    "otimista": 15.0 / T_REQ_MIN,                           # 0,2349
}

# ---------------------------------------------------------------- motores
# Catálogo Microred, 102-S: 0,7 A na máxima eficiência e 2,8 A bloqueado, a 12 V (8,4 W)
N_MOT = 3
P_MOT_CAT = 8.4     # W  (12 V x 0,7 A)
I_STALL = 2.8       # A  (a 12 V; limite superior, pois V_motor < 12 V)
# L298N (ST, jan. 2000): queda total VCEsat(H)+VCEsat(L) a IL = 1 A: 1,8 V típ., 3,2 V máx.
VSAT_TIP, VSAT_MAX = 1.8, 3.2
# L298N, corrente quiescente em VS (Ven = H, IL = 0, Vi = H): 70 mA máx.; em VSS (Vi = L): 36 mA máx.
IS_VS_MAX = 0.070
ISS_VSS_MAX = 0.036


def i_motor(vsat):
    """Corrente de cada motor com potência constante (premissa V.I ~ cte, instruções 11.5)."""
    v_m = V_NOM - vsat
    return P_MOT_CAT / v_m, v_m


# ---------------------------------------------------------------- eletrônica (limites superiores)
# Trilho de 5 V (MainBoard 2025: L7810 -> L7805, lineares): corrente na bateria = soma + Iq
I_PICO = 0.0955     # A - Pico datasheet, 3.1.1, Popcorn, power saving off, máx. a 85 °C (VBUS 5 V)
I_RADIO = 0.0135    # A - nRF24L01+ PS 1.0, tab. 4, RX 2 Mbps (maior que TX 0 dBm, 11,3 mA)
I_IR = 3.3 / 47     # A - esquemático main 2025 f.5: emissor IR com R12 = 47 ohm em 3,3 V (V/R)
I_LED33 = 3.3 / 100  # A - esquemático main 2025 f.1: LED D4 com R8 = 100 ohm em 3,3 V
I_BIAS = 5 * 3.3 / 10e3  # A - 4 resistores de ID + 1 de canal, 10 kohm em 3,3 V
I_ISO = 0.002 + 0.019    # A - ISO722x (SLLS755U), ICC1 + ICC2 máx. a 1 Mbps, 3,3 V
I_L298_VSS = N_MOT * ISS_VSS_MAX  # A
I_LED5 = 5.0 / 330  # A - LED D2 (R5 = 330 ohm) em 5 V
I_LEDKICK = 5.0 / 120  # A - LED D3 (R6 = 120 ohm) em 5 V, D = 1 (limite)
IQ_REG = 0.008      # A - L78 (DocID2143 rev. 33), Id do L7805C; mesmo limite adotado para o L7810
I_5V = (I_PICO + I_RADIO + I_IR + I_LED33 + I_BIAS + I_ISO
        + I_L298_VSS + I_LED5 + I_LEDKICK)
I_CADEIA = I_5V + 2 * IQ_REG
P_5V_SAIDA = 5.0 * I_5V
P_CADEIA_2025 = V_NOM * I_CADEIA      # linear: corrente de entrada = de saída + Iq

# Cargas ligadas direto em VBAT
I_LEDVBAT = 2 * V_NOM / 1e3          # LEDs VBAT (main R2 e kick R2 = 1 kohm)
I_DIV_BAT = V_NOM / 122e3            # divisor 100 k + 22 k
I_UCC = 0.00045                      # UCC27524A (SLUSBP4C), IVDDq máx.
P_VBAT = V_NOM * (I_LEDVBAT + I_DIV_BAT + I_UCC)
P_L298_VS = V_NOM * N_MOT * IS_VS_MAX

P_BASE = P_CADEIA_2025 + P_VBAT + P_L298_VS   # cargas com D = 1

# Alternativa 2026: LM2576HV-5.0 (SNVS107D: 77 % típ. a 12 V, 3 A)
ETA_LM2576 = 0.77
P_CADEIA_2026 = P_5V_SAIDA / ETA_LM2576
P_BASE_2026 = P_CADEIA_2026 + P_VBAT + P_L298_VS

# ---------------------------------------------------------------- chute
C_CAP = 2200e-6     # F - TDPs CBR 2025/2026; descritivo 2025
V_PROJ = 180.0      # V - TDPs CBR 2025/2026 ("up to 180 V")
V_ADC = 3.3 * (1e6 + 18e3) / 18e3   # V - teto do ADC: divisor 1 Mohm/18 kohm, ref. 3,3 V
V_CAPMAX = 200.0    # V - tensão nominal do capacitor (descritivo 2025)
I_L_MAX = 3.0       # A - indutor L0 100 uH / 3 A (BOM 2025; descritivo: >= 3 A)
R5 = 4.7e3          # ohm - resistor de descarga 2025 (5 W)
R_DESC_2026 = 10e3 / 2   # dois 10 kohm / 5 W em paralelo (esquemático kick 2026)


def e_cap(v):
    return 0.5 * C_CAP * v ** 2


def p_med(d_motor, vsat=VSAT_TIP, base=P_BASE):
    i_m, _ = i_motor(vsat)
    return base + N_MOT * V_NOM * i_m * d_motor


def t_op(p, f):
    return E_NOM * f / p


def margem(p, f, treq=T_REQ):
    return (t_op(p, f) - treq) / treq


def main():
    out = []
    pr = out.append
    pr(f"E_nom = {E_NOM:.2f} Wh ; t_req = {T_REQ:.4f} h ; limite P <= {E_NOM/T_REQ:.2f}*f W")
    for k, d in D_MOTOR.items():
        pr(f"D_motor {k}: {d:.4f}")
    i_t, vm_t = i_motor(VSAT_TIP)
    i_x, vm_x = i_motor(VSAT_MAX)
    pr(f"Motor: V_m tip = {vm_t:.2f} V, I = {i_t:.3f} A ; V_m min = {vm_x:.2f} V, I = {i_x:.3f} A")
    pr(f"P motores (3, D=1) bateria: tip {N_MOT*V_NOM*i_t:.2f} W ; max-queda {N_MOT*V_NOM*i_x:.2f} W ; "
       f"sem ajuste (0,7 A) {N_MOT*V_NOM*0.7:.2f} W")
    pr("--- eletrônica (limite superior)")
    for nome, i in [("Pico", I_PICO), ("radio", I_RADIO), ("IR", I_IR), ("LED 3V3", I_LED33),
                    ("bias", I_BIAS), ("ISO7220", I_ISO), ("L298 VSS x3", I_L298_VSS),
                    ("LED 5V", I_LED5), ("LED chute", I_LEDKICK)]:
        pr(f"  {nome:12s} {i*1e3:7.1f} mA")
    pr(f"  I_5V = {I_5V*1e3:.1f} mA ; I_cadeia = {I_CADEIA*1e3:.1f} mA ; P_saida5V = {P_5V_SAIDA:.2f} W")
    pr(f"  P cadeia 2025 (linear) = {P_CADEIA_2025:.2f} W ; eta_eq = {P_5V_SAIDA/P_CADEIA_2025:.3f} ; "
       f"dissipação = {P_CADEIA_2025-P_5V_SAIDA:.2f} W")
    pr(f"  P cadeia 2026 (LM2576, 77 %) = {P_CADEIA_2026:.2f} W ; economia = {P_CADEIA_2025-P_CADEIA_2026:.2f} W")
    pr(f"  P VBAT diretos = {P_VBAT:.3f} W ; P L298 VS x3 = {P_L298_VS:.2f} W")
    pr(f"  P_BASE 2025 = {P_BASE:.2f} W ; P_BASE 2026 = {P_BASE_2026:.2f} W")
    pr("--- P_med, f mínimo, margem")
    for k, d in D_MOTOR.items():
        for vs, lab in [(VSAT_TIP, "tip"), (VSAT_MAX, "max")]:
            p = p_med(d, vs)
            fmin = p * T_REQ / E_NOM
            ms = "  ".join(f"f={f:.1f}: M={margem(p, f)*100:+6.1f}%" for f in (0.6, 0.7, 0.8, 0.9))
            pr(f"{k:11s} queda {lab}: P_med={p:6.2f} W ; f_min={fmin:.3f} ; {ms}")
    pr("--- t_req alternativos (central, queda tip, f=0,8)")
    p = p_med(D_MOTOR["central"])
    for lab, t in [("63,85 min", T_REQ), ("60 min", T_EQUIPE), ("39,57 min", T_MEDIO)]:
        pr(f"  {lab}: M = {margem(p, 0.8, t)*100:+.1f}%")
    pr("--- corrente média máxima por motor que zera M (queda tip, f variável)")
    for k, d in D_MOTOR.items():
        for f in (0.6, 0.8):
            pdisp = E_NOM * f / T_REQ - P_BASE
            pm = pdisp / (N_MOT * d)          # potência por motor na bateria
            i_bat = pm / V_NOM
            pr(f"  {k:11s} f={f}: I_motor_max = {i_bat:.2f} A (na bateria)")
    pr("--- chute")
    for lab, v in [("projeto 180 V", V_PROJ), ("conferência ADC", V_ADC), ("limite cap 200 V", V_CAPMAX)]:
        pr(f"  {lab}: V = {v:.2f} V ; E = {e_cap(v):.2f} J ; R_min(20 A) = {v/20:.2f} ohm")
    pr(f"  aumento E ADC/projeto = {(e_cap(V_ADC)/e_cap(V_PROJ)-1)*100:.1f}%")
    for eta in (0.5, 0.7, 0.9):
        e_bat = e_cap(V_PROJ) / eta
        t_carga = e_cap(V_PROJ) / (eta * V_NOM * I_L_MAX)
        pr(f"  eta_b={eta}: energia/recarga na bateria = {e_bat:.1f} J ; t_carga_min = {t_carga:.2f} s")
    # recargas por partida que zeram M
    for k, d in D_MOTOR.items():
        for f in (0.6, 0.8):
            for eta in (0.5, 0.9):
                sobra_J = (E_NOM * f - p_med(d) * T_REQ) * 3600
                n = sobra_J / (e_cap(V_PROJ) / eta)
                pr(f"  N_max recargas {k:11s} f={f} eta={eta}: {n:8.0f} ({n/T_REQ_MIN:.1f}/min)")
    p_div = V_PROJ ** 2 / (1e6 + 18e3)
    pr(f"  divisor do capacitor a 180 V: {p_div*1e3:.1f} mW")
    pr("--- corrente de pico da bateria")
    i_ele = I_CADEIA + I_LEDVBAT + I_DIV_BAT + I_UCC + N_MOT * IS_VS_MAX
    i_pico = N_MOT * I_STALL + I_L_MAX + i_ele
    pr(f"  motores bloqueados {N_MOT*I_STALL:.1f} A + boost {I_L_MAX:.1f} A + eletrônica {i_ele:.3f} A = {i_pico:.2f} A")
    pr(f"  corrente máxima da bateria ({C_RATE} C) = {C_AH*C_RATE:.0f} A ; taxa exigida = {i_pico/C_AH:.2f} C")
    pr(f"  R_int max para V >= {V_MIN} V a partir de {V_NOM} V: {(V_NOM-V_MIN)/i_pico*1e3:.0f} mohm")
    for r in (0.02, 0.05, 0.10, 0.15):
        pr(f"  R_int={r*1e3:.0f} mohm: dV = {i_pico*r:.2f} V ; V = {V_NOM-i_pico*r:.2f} V")
    pr("--- descarga do capacitor")
    for lab, r, pn in [("2025 R5 4,7k/5W", R5, 5.0), ("2026 2x10k/5W", R_DESC_2026, 10.0)]:
        tau = r * C_CAP
        for v in (V_PROJ, V_ADC):
            pr(f"  {lab}: tau = {tau:.2f} s ; t(10%) = {tau*log(10):.1f} s ; P0 @ {v:.1f} V = {v**2/r:.2f} W (nominal {pn} W)")
    print("\n".join(out))


if __name__ == "__main__":
    main()
