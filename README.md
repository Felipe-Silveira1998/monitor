# 🔍 Monitor de Disponibilidade

Sistema completo de monitoramento de disponibilidade de produtos com alertas automáticos via email, WhatsApp e Telegram.

## 🚀 Acesso à Aplicação

**URL da Aplicação:** https://ogh5izce7qg1.manus.space

## 👨‍💼 Credenciais de Administrador

**Email:** admin@monitor.com  
**Senha:** Admin123!

## 📋 Funcionalidades

### Para Usuários
- ✅ **Cadastro e Login** - Sistema completo de autenticação
- ✅ **Criação de Alertas** - Monitore qualquer produto online
- ✅ **Múltiplos Canais** - Notificações via Email, WhatsApp e Telegram
- ✅ **Monitoramento Inteligente** - Detecta disponibilidade e mudanças de preço
- ✅ **Dashboard Personalizado** - Visualize todos os seus alertas
- ✅ **Histórico Completo** - Acompanhe o histórico de verificações

### Para Administradores
- ✅ **Gerenciamento de Usuários** - Visualizar e gerenciar todos os usuários
- ✅ **Estatísticas Globais** - Métricas de uso da plataforma
- ✅ **Monitoramento de Sistema** - Acompanhar performance dos alertas
- ✅ **Configurações Avançadas** - Ajustar parâmetros do sistema

## 🛠️ Como Usar

### 1. Primeiro Acesso
1. Acesse https://ogh5izce7qg1.manus.space
2. Clique em "Cadastro" para criar sua conta
3. Preencha: Nome, Email e Senha (mínimo 8 caracteres)
4. Faça login com suas credenciais

### 2. Criando um Alerta
1. Clique em "➕ Novo Alerta"
2. Preencha as informações:
   - **Nome:** Identifique seu alerta (ex: "Nintendo Switch 2")
   - **URL:** Link do produto que deseja monitorar
   - **Seletor CSS:** (Opcional) Para elementos específicos
   - **Palavra-chave:** (Opcional) Texto que indica disponibilidade
   - **Limite de Preço:** (Opcional) Alerta quando preço estiver abaixo
   - **Canais de Notificação:** Email, WhatsApp ou Telegram

### 3. Exemplos de Uso

#### Monitorar Nintendo Switch 2
```
Nome: Nintendo Switch 2 - Amazon
URL: https://amazon.com/nintendo-switch-2
Palavra-chave: em estoque, disponível
Canais: Email + WhatsApp
```

#### Monitorar Preço de Produto
```
Nome: iPhone 15 Pro - Desconto
URL: https://loja.com/iphone-15-pro
Limite de Preço: 999.99
Canais: Email + Telegram
```

#### Monitorar Vagas de Consulado
```
Nome: Consulado Italiano - Agendamento
URL: https://consulado.com/agendamento
Palavra-chave: vagas disponíveis, agendar
Canais: WhatsApp + Email
```

## 💡 Casos de Uso Populares

### 🛒 E-commerce
- Produtos em falta (Nintendo Switch, PS5, placas de vídeo)
- Ofertas e promoções especiais
- Black Friday e liquidações
- Lançamentos limitados

### 🏛️ Serviços Públicos
- Agendamento de consulados
- Vagas em concursos públicos
- Abertura de editais
- Disponibilidade de documentos

### 🏥 Saúde
- Agendamento de consultas médicas
- Disponibilidade de vacinas
- Abertura de agenda de especialistas
- Vagas em hospitais

### ✈️ Viagens
- Passagens aéreas em promoção
- Disponibilidade de hotéis
- Pacotes de viagem
- Vagas em voos

## 🔧 Configurações Avançadas

### Seletores CSS
Use seletores CSS para monitorar elementos específicos:
```css
.price-value          /* Preço do produto */
.stock-status         /* Status do estoque */
#availability         /* Disponibilidade */
.btn-buy              /* Botão de compra */
```

### Palavras-chave Eficazes
- **Disponibilidade:** "em estoque", "disponível", "comprar agora"
- **Indisponibilidade:** "fora de estoque", "esgotado", "indisponível"
- **Promoções:** "desconto", "oferta", "promoção", "liquidação"

## 📊 Dashboard e Estatísticas

O dashboard mostra:
- **Total de Alertas:** Quantidade de alertas criados
- **Disponíveis:** Produtos atualmente disponíveis
- **Indisponíveis:** Produtos fora de estoque
- **Ativos:** Alertas em monitoramento

## 🔐 Segurança

- ✅ Autenticação segura com hash de senhas
- ✅ Sessões protegidas
- ✅ Validação de dados de entrada
- ✅ Controle de acesso baseado em roles

## 🚀 Tecnologias Utilizadas

- **Backend:** Python Flask
- **Banco de Dados:** SQLite
- **Frontend:** HTML5, CSS3, JavaScript
- **Autenticação:** Flask-Login
- **Web Scraping:** BeautifulSoup + Requests
- **Notificações:** SMTP, WhatsApp API, Telegram Bot

## 📞 Suporte

Para dúvidas ou problemas:
1. Acesse a aplicação como administrador
2. Use as credenciais fornecidas acima
3. Verifique logs e estatísticas do sistema

## 🎯 Próximas Funcionalidades

- [ ] API REST completa
- [ ] Aplicativo mobile
- [ ] Integração com mais canais de notificação
- [ ] Machine Learning para detecção inteligente
- [ ] Relatórios avançados
- [ ] Webhooks personalizados

---

**Desenvolvido com ❤️ para automatizar seu monitoramento de produtos!**

