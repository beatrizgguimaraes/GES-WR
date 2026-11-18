# Distribuição do tempo de partida por fase (SSL Divisão B) — referência de ordem de grandeza para os D_i do módulo de Orçamentos

Versão 7, 11/11/2026. Mudanças em relação à v6: (a) a bateria ligada no intervalo e no timeout está decidida (FFJ, 11/11/2026; autora): premissa do trabalho, pior caso (seção 6 e texto da seção 8.4); (b) as instruções do projeto já estão com t_req = 63,85 min (v3.3; seção 7); (c) fontes registradas conforme a seção 11.9 das instruções: URL da página da SSL para o painel da Tigers e URL das regras da SSL 2026 (seções 1 e 8.3); (d) HALT e STOP definidos pelas regras da SSL, seções 5.1.1 e 5.1.2, decisão da autora (seções 1, 8.4, 8.5 e 8.6); (e) cenários de D_motor referenciados ao `status_entregas` v2.2 (seção 8.1). Mudanças da v6 em relação à v5: (a) t_req adotado de 63,85 min, decisão da autora (seção 7); (b) a categoria SSL da CBR segue as regras da SSL, decisão da autora (seção 1). Mudanças da v5 em relação à v4: (a) o painel passa a ser usado só como ordem de grandeza e checagem cruzada, e seus números são identificados como agregados da Divisão B (seção 1 e 8.1); (b) nova seção 7, que registra o t_req informado pela equipe (60 min) e o calculado pelas métricas do painel (63,85 min); (c) a fonte dos 40 min e dos 60 min passa a ter data e interlocutor; (d) o texto LaTeX foi atualizado. As tabelas das seções 5 e 6 não mudaram. Elaborado pela autora a partir de dados do painel RoboCup 2025 Div. B e das regras da SSL 2026.

## 1. Fontes
- Fração do tempo por fase (média de todas as partidas): painel de métricas RoboCup 2025 Div. B, Metabase (TIGERs Mannheim), arquivo `DISCLAIMER_merged_compressed.pdf`, impresso em 27/10/2026. URL do painel: https://metabase.tigers-mannheim.de/public/dashboard/3e16b3b1-b3a0-412c-ba5a-a52e441dc6cd?division=DivB&tournament=RoboCup2025. Caminho pela página da SSL: https://ssl.robocup.org/match-statistics/, em "Interactive statistics", com a visualização atribuída à TIGERs Mannheim (decisão da autora, seção 11.9 das instruções). Ano de publicação: VERIFICAR.
- Definição das fases HALT e STOP: as das regras da SSL, seções 5.1.1 (Stop) e 5.1.2 (Halt) (decisão da autora, 11/11/2026). A definição interna do painel para cada fase não foi verificada (ver seção 8.5).
- Escopo do painel: os números são agregados da Divisão B da RoboCup 2025. O aviso na primeira página do arquivo diz que as informações que mencionam o Warthog são do Time A e que a competição não contou com o Time B. Os números não são medições do Time B.
- Durações por fase: SSL Rules 2026, seção 4.4.1 (estágios do jogo) e 4.4.2 (timeouts); as regras 2025 têm os mesmos valores. URL: https://ssl.robocup.org/rules/. Autor, título, ano e data de acesso: VERIFICAR.
- CBR: a categoria SSL da CBR segue as regras da SSL (autora, 11/11/2026). Fonte citável dispensada pela autora.
- Duração de partida informada pela equipe: média de 40 min e pior caso de 60 min (1 h). Fonte: comunicação pessoal, FFJ, 09/11/2026 (no texto, usar "gerente do projeto Lyra").

## 2. Jogos de referência
- **Jogo médio, 40 min de referência:** jogo disputado em dois tempos completos, sem prorrogação.
- **Jogo longo, 60 min de referência:** jogo completo (dois tempos completos) mais prorrogação completa.

## 3. Duração das fases segundo as regras
| Fase | Natureza | Jogo médio (40 min) | Jogo longo (60 min) |
| --- | --- | --- | --- |
| RUNNING (tempo de jogo) | Fixa (cronômetro) | 10 min (2 × 300 s) | 15 min (600 s + 2 × 150 s) |
| BREAK (intervalos) | Fixa (pausa definida) | 5 min (300 s) | 12 min (300 + 300 + 120 s) |
| TIMEOUT | Variável, com teto | ≤ 10 min (2 times × 300 s) | ≤ 15 min (600 s + 2 times × 150 s) |
| HALT, STOP, Outros | Variável, sem teto fixo | — | — |

Premissa: sem encerramento antecipado por 10 gols (SSL 2026, 4.4.3) e sem intervalo encurtado.

## 4. Método
1. Aplica-se cada percentual do painel ao tempo de referência (40 ou 60 min).
2. Fase que respeita a regra: o percentual do painel é mantido.
3. Fase fixa cujo valor não coincide com a regra (RUNNING e BREAK): o percentual passa a ser (valor da regra) / (tempo de referência).
4. Os percentuais das demais fases não são alterados nem redistribuídos. O ajuste vai para o total: o tempo total do jogo passa a ser a soma das fases, e o total de percentuais deixa de ser 100 %.

## 5. Tabela final
| Fase | Painel (%) | 40 min: % | 40 min: min | 60 min: % | 60 min: min |
| --- | --- | --- | --- | --- | --- |
| RUNNING | 24,88 | **25,00** (*) | 10,00 | **25,00** (*) | 15,00 |
| HALT | 25,94 | 25,94 | 10,38 | 25,94 | 15,56 |
| STOP | 21,73 | 21,73 | 8,69 | 21,73 | 13,04 |
| BREAK (intervalo) | 13,70 | **12,50** (*) | 5,00 | **20,00** (*) | 12,00 |
| TIMEOUT | 10,18 | 10,18 | 4,07 | 10,18 | 6,11 |
| Outros | 3,57 | 3,57 | 1,43 | 3,57 | 2,14 |
| **Total** | 100,00 | **98,92** | **39,57** | **106,42** | **63,85** |

(*) Percentual alterado para respeitar a regra. Os demais são os do painel.
Os totais são a soma das linhas: 40 min × 98,92 % = 39,57 min; 60 min × 106,42 % = 63,85 min.

## 6. Fração do tempo total ajustado (referência para os D_i)
Como os percentuais da seção 5 não somam 100 %, a fração de tempo de cada fase em relação ao jogo ajustado é (minutos da fase) / (total ajustado). Estas frações somam 100 %.

| Fase | Jogo médio (39,57 min) | Jogo longo (63,85 min) |
| --- | --- | --- |
| RUNNING | 25,27 % | 23,49 % |
| HALT | 26,22 % | 24,38 % |
| STOP | 21,97 % | 20,42 % |
| BREAK | 12,64 % | 18,79 % |
| TIMEOUT | 10,29 % | 9,57 % |
| Outros | 3,61 % | 3,35 % |
| **Total** | 100,00 % | 100,00 % |

Notas:
- "Outros" = ball placement, post game, prepare kickoff e prepare penalty.
- A bateria permanece ligada durante todo o intervalo t_req; as cargas em espera entram no P_med com o seu próprio D_i. Decidido em 11/11/2026 (FFJ e autora): a bateria nem sempre fica ligada no intervalo e no timeout, mas geralmente fica, e o trabalho considera que fica ligada, como pior caso para o consumo de energia. O texto deve mencionar que nem sempre é assim (seção 8.4).

## 7. Comparação com o t_req
| Origem | t_req (min) | Como foi obtido |
| --- | --- | --- |
| Informado pela equipe em entrevista | 60 (1 h) | Pior caso de duração de partida (comunicação pessoal, FFJ, 09/11/2026) |
| Calculado pelas métricas da Tigers e pelas regras | 63,85 | Jogo longo: 60 min de referência × 106,42 % (seção 5) |

- Diferença: 3,85 min (6,4 % acima de 60 min).
- Origem da diferença: o intervalo fixado em 12 min pelas regras, contra 8,22 min que resultam do percentual do painel (13,70 % de 60 min), responde por 3,78 min dos 3,85 min. O tempo de jogo (15 min contra 14,93 min) responde pelo resto.
- Os dois valores são registrados no trabalho.
- **Decisão da autora (11/11/2026): t_req = 63,85 min** (1,0642 h), com a bateria ligada. O jogo longo da seção 6 tem exatamente essa duração, então as frações dele valem sobre o t_req.
- Consequência na condição de autonomia: P_med ≤ C · V_nom · f / t_req = 57,72 Wh · f / 1,0642 h ≈ 54,24 · f W (com C = 5,2 Ah e V_nom = 11,1 V; f a definir com fonte).
- As instruções do projeto (seções 11.5 e 11.9) já estão com t_req = 63,85 min (v3.3, 11/11/2026).

## 8. Uso dos dados e como citar no trabalho

### 8.1 Escopo do uso
- O painel é usado como ordem de grandeza e checagem cruzada dos fatores de uso D_i, e não como medição do Time B. Os números são da Divisão B da RoboCup 2025, em que o Time B do Warthog não participou (aviso na primeira página do arquivo).
- As frações da seção 6 servem de referência para os cenários de D_motor do `status_entregas` (v2.2). Sobre o jogo longo, que vale sobre o t_req: central 0,47 (Running + Stop + Outros), conservador 1 e otimista ≈ 0,235 (só Running).

### 8.2 Regras de citação
1. Todo percentual de fase (colunas "Painel" e as frações derivadas deles) vem do painel do RoboCup 2025 Div. B. Sempre que um desses números aparecer no texto, em tabela ou em equação, citar o painel (`\cite{tigers2025painel}`) e dizer que são agregados da Divisão B.
2. Toda duração fixa (RUNNING, BREAK) e todo teto de TIMEOUT vem das regras da SSL 2026, seções 4.4.1 e 4.4.2. Citar as regras (`\cite{ssl2026regras}`), indicando a seção. As definições de HALT e STOP vêm das seções 5.1.1 e 5.1.2.
3. As durações de 40 min (média) e 60 min (pior caso) são da equipe: citar como comunicação pessoal (gerente do projeto Lyra, 09/11/2026).
4. O método de ajuste (seção 4 deste arquivo), os jogos de referência, as frações da seção 6, o valor de 63,85 min e a decisão de manter os percentuais do painel e ajustar o total são da autora. Na legenda, usar "adaptado de" e "elaborado pela autora".
5. Legenda e fonte da tabela da seção 5: "Fonte: adaptado de \citeonline{tigers2025painel}, com durações de \citeonline{ssl2026regras}; elaborado pela autora."

### 8.3 Entradas BibTeX (completar os campos marcados)
```bibtex
@misc{tigers2025painel,
  author  = {{TIGERs Mannheim}},
  title   = {Overall Tournament Metrics: RoboCup 2025, Division B},
  howpublished = {Painel Metabase},
  url     = {https://metabase.tigers-mannheim.de/public/dashboard/3e16b3b1-b3a0-412c-ba5a-a52e441dc6cd?division=DivB&tournament=RoboCup2025},
  urldate = {2026-10-27},
  note    = {VERIFICAR: ano de publicação e se há descrição oficial dos dados. Caminho pela página da SSL: https://ssl.robocup.org/match-statistics/ (Interactive statistics), que atribui a visualização à TIGERs Mannheim (seção 11.9 das instruções). A data de acesso é a da impressão do PDF.}
}

@misc{ssl2026regras,
  title = {VERIFICAR: título oficial das regras da SSL 2026},
  url   = {https://ssl.robocup.org/rules/},
  note  = {VERIFICAR: autor/órgão responsável, ano e data de acesso. Seções usadas: 4.4.1, 4.4.2, 4.4.3, 5.1.1 e 5.1.2. Arquivo do projeto: ssl rules 2026.pdf}
}
```

### 8.4 Texto-base para o capítulo (LaTeX), com a explicação da definição
```latex
\subsection{Distribuição do tempo de partida por fase de jogo}
\label{sec:tempo-partida}

A fração do tempo de uma partida da SSL em cada fase de jogo foi tomada do painel
de métricas do RoboCup 2025, Divisão B \cite{tigers2025painel}. Para o conjunto de
partidas da divisão, o painel informa a parcela do tempo total em cada fase:
\emph{running}, \emph{halt}, \emph{stop}, intervalo (\emph{break}), \emph{timeout}
e as demais fases (\emph{ball placement}, \emph{post game}, \emph{prepare kickoff}
e \emph{prepare penalty}), reunidas em ``outros''. As fases \emph{halt} e \emph{stop}
são as definidas pelas regras da liga \cite[seções 5.1.1 e 5.1.2]{ssl2026regras}.
Os valores são agregados da Divisão B desse torneio, no qual o Time B do Warthog
não participou. Por isso, não representam medições do Time B e foram usados como
ordem de grandeza e checagem cruzada dos fatores de uso $D_i$. Os percentuais
foram mantidos sem alteração, exceto quando contrariam as durações definidas pelas
regras da liga \cite{ssl2026regras}.

Foram definidos dois jogos de referência. O jogo médio, de 40 min, é disputado em
dois tempos completos, sem prorrogação, e a duração adotada é a estimativa da
equipe (comunicação pessoal, gerente do projeto Lyra, 09/11/2026). O jogo longo, de
60 min, é disputado em dois tempos completos e prorrogação completa. Segundo as
regras \cite[seções 4.4.1 e 4.4.2]{ssl2026regras}, o tempo de jogo e os intervalos
têm duração fixa: 10~min de jogo e 5~min de intervalo no jogo médio, e 15~min de
jogo e 12~min de intervalo no jogo longo. O tempo de \emph{timeout} é variável,
limitado a 10~min no jogo médio e a 15~min no jogo longo.

Para cada jogo de referência, o percentual do painel foi aplicado ao tempo de
referência. Quando o resultado de uma fase de duração fixa diferia do valor
definido pelas regras, o percentual dessa fase foi substituído pela razão entre
o valor da regra e o tempo de referência. Isso ocorreu para o tempo de jogo e
para o intervalo. Os percentuais das demais fases foram mantidos e não foram
redistribuídos, de modo que o ajuste recaiu sobre o tempo total, que passou a
ser a soma das fases: 39,57~min no jogo médio e 63,85~min no jogo longo
(Tabela~\ref{tab:tempo-fases}). Por fim, dividiu-se o tempo de cada fase pelo
tempo total ajustado, para que as frações somassem 100\% e servissem de
referência ao ciclo de uso $D_i$ (Tabela~\ref{tab:fracao-tempo}). Considerou-se
que não há encerramento antecipado da partida nem intervalo encurtado.

A equipe informou em entrevista 60~min como pior caso de duração de partida
(comunicação pessoal, gerente do projeto Lyra, 09/11/2026). O jogo longo calculado
a partir das métricas do painel \cite{tigers2025painel} e das durações das regras
\cite{ssl2026regras} tem 63,85~min, ou seja, 3,85~min (6,4\%) a mais. A diferença
vem quase toda do intervalo, fixado em 12~min pelas regras, contra 8,22~min que
resultariam do percentual do painel. Adotou-se $t_{\mathrm{req}} = 63{,}85$~min,
valor que cobre o jogo longo completo, com a bateria ligada durante todo o
intervalo. Considerou-se a bateria ligada também no intervalo entre tempos e nos
\emph{timeouts}. A equipe informou que isso nem sempre ocorre, mas costuma ocorrer
(comunicação pessoal, gerente do projeto Lyra, 11/11/2026), e a hipótese adotada é
a de pior caso para o consumo de energia. A categoria SSL da Competição Brasileira
de Robótica (CBR) segue as regras da SSL, de modo que as durações aqui usadas
valem para o Time B.
```

### 8.5 Limitações a registrar no capítulo
- O painel traz a média de todas as partidas da Divisão B; aplicá-la a um jogo de 40 ou 60 min supõe a mesma proporção de pausas em qualquer jogo.
- Os números são da Divisão B da RoboCup 2025, em que o Time B não participou; eles não medem o Time B nem a CBR.
- O trabalho adota as definições de HALT e STOP das regras da SSL (5.1.1 e 5.1.2), mas a definição interna de cada fase no painel (em especial HALT) não foi verificada na fonte. Se o HALT do painel incluir tempo fora das partidas, as frações de HALT e STOP podem estar superestimadas.
- Os percentuais do painel são de um torneio (RoboCup 2025 Div. B); a generalização para outros torneios é uma ameaça à validade externa.
- A bateria ligada no intervalo e no timeout é premissa de pior caso: nem sempre ocorre (FFJ, 11/11/2026).

### 8.6 Pendências deste arquivo
- Completar a entrada `ssl2026regras` (autor, título, ano e data de acesso; a URL já está registrada) e conferir a de `tigers2025painel` (ano de publicação).

Resolvidas em 11/11/2026:
- Definição das fases HALT e STOP: adotada das regras da SSL, seções 5.1.1 e 5.1.2 (decisão da autora). A definição interna do painel segue como limitação (seção 8.5).
- Instruções do projeto (seções 11.5 e 11.9) atualizadas para t_req = 63,85 min (v3.3).
- Bateria ligada no intervalo e no timeout: confirmado pelo FFJ como "geralmente sim", e adotado como pior caso.
