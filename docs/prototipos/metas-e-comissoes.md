---
icon: lucide/target
title: Metas e Comissões
---

# Metas e Comissões

Tela nova, montada com a mesma composição do [Acompanhamento Mensal](acompanhamento-mensal.md): três indicadores, uma tabela e o calendário do mês. Mostra as comissões do operador sobre as parcelas pagas.

| | |
| --- | --- |
| Origem | **Criado no Figma**, duplicando o Acompanhamento Mensal |
| Nó no Figma | [62:2126](https://www.figma.com/design/jEwHxavSrPVQrm3hGSLGtC/edson-alexandre-advogados_design-system?node-id=62-2126) |
| Fonte no repositório | não existe; a base é `ui_kits/plataforma_processos/Prazos.jsx` |
| Componentes | `SidebarNav`, `TopBar`, `MetricCard` (três), `DataTable`, calendário mensal |
| Histórias de usuário | [US32](../historias/ep05-comissoes-metas.md#us32) (minhas comissões) e [US33](../historias/ep05-comissoes-metas.md#us33) (visão global), sem distinguir os dois perfis; [US36](../historias/ep05-comissoes-metas.md#us36) (definir metas por colaborador) não tem tela. Ver a [cobertura das histórias](cobertura-historias.md). |

## O que a tela mostra

**Indicadores**: metas acumuladas no mês R$ 1.250,00; Acordos fechadas 8; Taxa de conversão de promessas 52%.

**Tabela**, com colunas Acordo (Condomínio), Data do Pagamento, Parcela, Valor total pago, Valor honorários e Comissão Operador:

| Acordo (Condomínio) | Data do Pagamento | Parcela | Valor total pago | Valor honorários | Comissão Operador |
| --- | --- | --- | --- | --- | --- |
| Cond. Lake View | 09/09/2026 | 01/06 | R$ 500,00 | R$ 50,00 | R$ 15,00 |
| Cond. Jardins do Sul | 05/09/2026 | 03/03 | R$ 400,00 | R$ 80,00 | R$ 24,00 |
| Res. Terra Nova | 02/09/2026 | 08/12 | R$ 600,00 | R$ 60,00 | R$ 18,00 |

**Calendário** de setembro de 2026, ainda com os marcadores "Prazo fatal" e "Prazo".

!!! info "Captura pendente"

    Este frame foi criado no Figma e ainda não tem captura exportada. Abra o [nó 62:2126](https://www.figma.com/design/jEwHxavSrPVQrm3hGSLGtC/edson-alexandre-advogados_design-system?node-id=62-2126) ou exporte o frame em PNG a 1x como `assets/prototipos/metas-e-comissoes.png`.

## Pontos de atenção

- "Acordos fechadas" tem erro de concordância: "Acordos fechados".
- "metas acumuladas no mês" está em caixa baixa e é ambíguo: o valor parece ser a comissão acumulada, não a meta. O protótipo de requisito "Faturas do mês" separa "Minha meta do mês" (valor recuperado sobre a meta, em barra de progresso) de "Comissão acumulada".
- A tela mistura a visão do operador (minhas comissões) com a do administrador (metas da equipe). Os protótipos de requisito tratam como duas telas com perfis diferentes; decida se aqui há uma tela com duas abas ou duas telas.
- As proporções variam entre linhas: honorários de 10%, 20% e 10% sobre o valor pago, comissão de 30% sobre os honorários. O protótipo HTML usa 8% de comissão. Fixe a regra antes de espalhar números.
- O calendário e seus marcadores vieram do Acompanhamento Mensal e não têm função clara aqui. Um gráfico de atingimento da meta no mês diz mais.
