# Política de Segurança

## 🔒 Recursos de Segurança Implementados

### Configuração de Recursos Externos

- **Crossorigin**: Configuração adequada de CORS para recursos de terceiros
- **Referrer Policy**: Controle de informações de referência enviadas para domínios externos
- **Versões Específicas**: Uso de versões específicas dos CDNs quando possível

### Content Security Policy (CSP)

- **CSP Headers**: Políticas configuradas para permitir recursos HTTPS confiáveis
- **Script Sources**: Permite scripts de CDNs confiáveis e inline necessário para funcionalidade
- **Connect Sources**: Restrições nas conexões para APIs (apenas Google Gemini API)
- **Img Sources**: Controle de fontes de imagens incluindo data: e blob: para PDFs

### Validação e Sanitização de Entrada

- **Sanitização de Prompts**: Limpeza automática de inputs para prevenir injeção de código
- **Validação de API Key**: Verificação de formato da chave de API do Google AI Studio
- **Validação de Arquivos**:
  - Verificação de tipo MIME (apenas PDF)
  - Limite de tamanho máximo (10MB)
  - Validação de conteúdo

### Rate Limiting

- **Controle de Frequência**: Limite de 2 segundos entre requisições para a API
- **Prevenção de Abuso**: Proteção contra uso excessivo da aplicação

### Segurança de Links e Navegação

- **rel="noopener noreferrer"**: Todos os links externos são seguros
- **Target="_blank"**: Links externos abrem em nova aba sem acesso ao contexto original
- **Validação de URLs**: Verificação de URLs antes do redirecionamento

### Tratamento Seguro de Erros

- **Timeout de Requisições**: Limite de 30 segundos para evitar travamentos
- **Error Handling**: Tratamento seguro de exceções sem exposição de dados sensíveis
- **User Agent**: Identificação adequada nas requisições HTTP
- **Logging Seguro**: Logs de erro sem exposição de informações confidenciais

### Proteção de Dados

- **Processamento Local**: Toda a manipulação de dados ocorre no navegador do usuário
- **Não Armazenamento**: Dados não são persistidos no servidor ou localStorage
- **API Key Segura**: Chaves de API são utilizadas apenas em memória

## 🚨 Relatório de Vulnerabilidades

Se você descobrir uma vulnerabilidade de segurança, por favor:

1. **NÃO** abra uma issue pública
2. Envie um email para o desenvolvedor descrevendo:
   - Tipo de vulnerabilidade
   - Passos para reproduzir
   - Impacto potencial
   - Sugestões de correção (se houver)

## 📋 Checklist de Segurança

- ✅ Content Security Policy configurada
- ✅ Configuração segura de recursos externos (crossorigin, referrer policy)
- ✅ Validação de entrada implementada
- ✅ Rate limiting ativo
- ✅ Links externos seguros
- ✅ Tratamento seguro de erros
- ✅ Timeout em requisições
- ✅ Sanitização de dados
- ✅ Validação de tipos de arquivo
- ✅ Proteção contra XSS
- ✅ Validação de API Keys
- ✅ Processamento local de dados (não armazenamento no servidor)

## 🔄 Atualizações de Segurança

Este documento é atualizado sempre que novos recursos de segurança são implementados ou quando vulnerabilidades são corrigidas.

**Última atualização**: 22 de junho de 2025
