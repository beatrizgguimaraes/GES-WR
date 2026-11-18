# GES-WR

**Guia de Engenharia de Sistemas para o Warthog Robotics** — ferramenta-guia, adaptada das normas
ISO/IEC/IEEE 15288, 29148 e 42010, que conduz a equipe do conceito de operações (ConOps) à arquitetura
física de robôs autônomos, com orçamento de energia e rastreabilidade entre os artefatos.

Desenvolvida como Trabalho de Conclusão de Curso:

> GUIMARÃES, Beatriz Gonçalves. *Ferramenta-guia de engenharia de sistemas para projetos de hardware
> de robôs autônomos: proposta e aplicação no Warthog Robotics*. Trabalho de Conclusão de Curso
> (Engenharia Elétrica com ênfase em Sistemas de Energia e Automação) — Escola de Engenharia de
> São Carlos, Universidade de São Paulo, São Carlos, 2026.
> Orientador: Prof. Dr. Ivan Nunes da Silva.

**Versão da ferramenta:** 1.1 (versão avaliada no Capítulo 4 do TCC).

## Conteúdo do repositório

| Pasta ou arquivo | O que contém |
|---|---|
| `ferramenta/` | O arquivo da ferramenta GES-WR, versão 1.1 |
| `exemplo/` | Exemplo de aplicação ao robô do Time B de 2025: dados "antes" e "depois" (.json) e o programa que os monta |
| `calc/` | Script da análise elétrica do Capítulo 4 |
| `dados/` | Tabela de distribuição do tempo de partida por fase de jogo da SSL |
| `SHA256SUMS.txt` | Valores de SHA-256 dos arquivos da versão avaliada, para conferir que são os mesmos citados na monografia |

O guia de uso da ferramenta está no Apêndice A do TCC.

## Conferir a integridade dos arquivos

Na pasta do repositório, em um terminal:

```bash
sha256sum -c SHA256SUMS.txt
```

Cada linha deve terminar em `OK`. No Windows, sem terminal Unix, use `certutil -hashfile ARQUIVO SHA256`
e compare com o valor de `SHA256SUMS.txt`.

## Documentos não incluídos

Este repositório não contém os documentos do Time B de 2025 e 2026 (TDPs, esquemáticos, listas de
materiais, descritivos), que são documentos internos do Programa Hercules, nem os textos das normas
ISO/IEC/IEEE, que são protegidos por direitos autorais. Os dados de entrada do exemplo foram
transcritos desses documentos e estão identificados em cada item pela fonte.

Os percentuais de tempo por fase de jogo vêm de um painel público da TIGERs Mannheim (RoboCup 2025,
Divisão B) e as durações, das regras da RoboCup Small Size League. Esses materiais pertencem aos
respectivos autores, e a licença deste repositório não se aplica a eles.

## Como citar

Veja o arquivo [`CITATION.cff`](CITATION.cff). O GitHub mostra a opção **Cite this repository** na
página do repositório.

## Licença

Código, ferramenta e dados deste repositório sob a licença MIT (arquivo [`LICENSE`](LICENSE)),
exceto os materiais de terceiros citados acima.
