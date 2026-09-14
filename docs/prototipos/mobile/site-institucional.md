---
icon: lucide/globe
title: Site institucional
---

# Site institucional (mobile)

Landing page do escritório em uma coluna, com as mesmas dez seções do site: navegação, hero, áreas de atuação, faixa clara de atendimento online, assessoria para condomínios, avaliações, equipe, formulário de contato, visita e rodapé. As seções de marketing continuam centralizadas, como manda a marca; os cards de área empilham em uma coluna e a equipe vira uma fileira rolável.

| | |
| --- | --- |
| Arquivo | `prototipos/mobile/site-institucional.html` no repositório [`Advocondo/ui-kit`](https://github.com/Advocondo/ui-kit) |
| Histórias de usuário | [US01](../../historias/ep01-portal-autenticacao.md#us01) |
| Estados | `?menu` — menu de seções aberto<br>`?enviado` — formulário de contato enviado |
| Componentes do design system | `Logo`, `SectionTitle`, `PracticeCard`, `TeamCard`, `Card tone="onNavy"`, `Button` (`primary`, `outline` sobre navy), `IconButton`, `Input`, `Textarea`, `Alert`, `Icon` |
| Navegação | Página pública, sem barra de navegação da plataforma. "Entrar" no cabeçalho e "Acessar a plataforma" no hero levam ao Login. |
| Versão desktop | [Site institucional](../site-institucional.md) |

## Capturas

Capturas em 390px de largura, renderizadas do HTML. As telas longas aparecem inteiras; as de diálogo, na altura de um aparelho (844px).

<figure markdown="span">

![Página completa](../../assets/prototipos/mobile/site-institucional.png)

<figcaption>Página completa</figcaption>

</figure>

<figure markdown="span">

![Menu de seções aberto](../../assets/prototipos/mobile/site-institucional-menu.png)

<figcaption>Menu de seções aberto</figcaption>

</figure>

## O que muda em relação ao Figma

- O ponto de entrada para o Login, que faltava no Figma, aparece duas vezes: no cabeçalho e como botão de contorno no hero.
- As estrelas das avaliações usam navy, não âmbar: os matizes semânticos não entram no site institucional.
- O formulário tem estado de sucesso inline (`Alert tone="ok"`) em vez de página separada.

## Premissas

- Copy do site atual, com o ponto de entrada para o Login que a US01-CA03 pede.
- Fotos da equipe ausentes: TeamCard mostra o placeholder navy do componente.
- Avaliações parafraseadas; substituir pelos reviews reais antes de uso público.

## Pontos de atenção

- As fotos da equipe continuam ausentes; os retratos usam o placeholder do `TeamCard`.
- Os textos das avaliações seguem parafraseados. Substitua pelos reviews reais antes de uso público.
