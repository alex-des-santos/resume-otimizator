# Assistente de Carreira com IA – Otimizador de Currículo

Otimize seu currículo, prepare-se para entrevistas e fortaleça sua presença profissional usando inteligência artificial generativa.

## ✨ Funcionalidades
- **Otimização de Currículo para ATS**: Reescreva seu currículo para maximizar a compatibilidade com a vaga desejada, usando IA.
- **Análise de Currículo**: Receba feedback detalhado sobre pontos fortes e melhorias.
- **Geração de Perguntas de Entrevista**: Obtenha perguntas personalizadas para se preparar melhor.
- **Carta de Apresentação**: Crie cartas de apresentação alinhadas à vaga.
- **Otimização de LinkedIn**: Sugestões para fortalecer seu perfil profissional.
- **Follow-up Profissional**: Modelos de mensagens para acompanhamento após entrevistas.
- **Pitch Profissional**: Gere um pitch de apresentação pessoal.
- **Respostas no Formato STAR**: Respostas estruturadas para entrevistas comportamentais.
- **Exportação em PDF**: Baixe o currículo otimizado em PDF.

## 🚀 Como Usar
1. Abra o arquivo `index.html` em seu navegador.
2. Insira sua chave da API Gemini, a descrição da vaga e faça upload do seu currículo em PDF.
3. Clique em **Gerar Currículo Otimizado**.
4. Utilize os botões de funcionalidades extras para gerar análises, perguntas, cartas, pitch, etc.
5. Visualize o resultado e faça o download em PDF.

## 🛠️ Tecnologias Utilizadas
- **Frontend**: HTML5, Tailwind CSS, JavaScript (ES6+)
- **IA**: Integração com Google Gemini API
- **PDF**: pdf.js e jsPDF para leitura e exportação
- **Markdown**: marked.js para visualização

## 📦 Requisitos
- Navegador moderno (Chrome, Edge, Firefox, etc.)
- Chave de API Gemini válida (Google)

## � Recursos de Segurança

### Integridade de Subrecursos (SRI)
- **SRI Hashes**: Todos os recursos externos (CDN) possuem hashes SHA-384 para verificar integridade
- **Crossorigin**: Configuração adequada de CORS para recursos de terceiros
- **Referrer Policy**: Controle de informações de referência enviadas

### Content Security Policy (CSP)
- **CSP Headers**: Políticas restritivas para prevenir ataques XSS
- **Script Sources**: Apenas scripts de origens confiáveis são permitidos
- **Style Sources**: Controle rigoroso de fontes de CSS

### Validação de Entrada
- **Sanitização**: Limpeza automática de inputs para prevenir injeção de código
- **Validação de API Key**: Verificação de formato da chave de API
- **Validação de Arquivo**: Verificação de tipo e tamanho máximo (10MB)
- **Rate Limiting**: Limite de 2 segundos entre requisições para prevenir abuso

### Segurança de Links
- **rel="noopener noreferrer"**: Todos os links externos são seguros
- **Target="_blank"**: Links externos abrem em nova aba sem acesso ao contexto original

### Tratamento de Erros
- **Timeout**: Requisições com limite de 30 segundos
- **Error Handling**: Tratamento seguro de exceções sem exposição de dados sensíveis
- **User Agent**: Identificação adequada nas requisições HTTP

## �📄 Licença
MIT. Veja o arquivo [LICENSE](LICENSE).

---
[Otimizador de Currículo](https://alex-des-santos.github.io/resume-otimizator/)

Desenvolvido por Alexandre. Para dúvidas ou sugestões, abra uma issue ou entre em contato.
