# README Técnico - Plataforma de Cadastro em Saúde 🏥
# 🚀 Visão Geral
Sistema de gerenciamento de pacientes desenvolvido em Python, evoluindo de uma implementação básica para uma versão com persistência de dados.

# 📈 Evolução das Versões
  ## v0.0.1 → v0.0.2: Principais Melhorias
  |Funcionalidade |	v0.0.1 |	v0.0.2 |
  |--- |--- |--- |
  |Persistência de dados |	❌ Memória apenas |	✅ JSON |
  |Tratamento de diretórios |	❌ |	✅ Criação automática |
  |Modo demonstração |	❌ |	✅ Opção de dados exemplo |
  |Recuperação de erro |	Básico |	✅ Melhor tratamento de exceções |
  |Estrutura de código |	Monolítica |	✅ Funções modularizadas |

  ## Novas Funcionalidades na v0.0.2
  
  1. ### Sistema de Persistência JSON
```python
DATA_DIR = "data_saúde"
ARQUIVO_JSON = os.path.join(DATA_DIR, "pacientes.json")
```
    
  2. ### Modo Demonstração Inteligente
     - Opção de usar dados de exemplo quando o arquivo não existe.
     - Indicação clara do modo de operação
  
  3. ### Gerenciamento de Diretório
```python
def garantir_diretorio():
Path(DATA_DIR).mkdir(parents=True, exist_ok=True)
```

   4. ### Carregamento Adaptativo
      - Detecta automaticamente se é a primeira execução
      - Oferece opções ao usuário

# 🔧 Como Executar
## Pré-requisitos
- Python 3.6+
- Permissões de escrita no sistema de arquivos

# 🎯 Funcionalidades Detalhadas
## Cadastro de Pacientes
- Validação de nome (sem números, não vazio)
- Validação de idade (inteiro positivo)
- Formatação automática de telefone ((XX) XXXXX-XXXX)

## Estatísticas
- Cálculo em tempo real
- Identificação de extremos (mais novo/velho)
- Média aritmética simples

## Busca
- Busca parcial por nome
- Case-insensitive
- Exibição de múltiplos resultados

# 🚀 Melhorias Futuras Detalhadas
## Prioridade Alta
### 1. Sistema de Autenticação
   - Implementar login de usuários
   - Controle de acesso baseado
   - Registros de mudança no arquivo

### 2. Backup e Restauração
```python
# Exemplo de implementação futura
def backup_automatico():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"backup_pacientes_{timestamp}.json"
    # Lógica de backup
```
        
### 3. Validação Avançada
  - Verificação de CPF único
  - Validação de telefone via API
  - Verificação de duplicatas

## Prioridade Média
### Interface Web
  - Migração para Flask/Django
  - Frontend responsivo

### Relatórios Avançados
  - Gráficos de distribuição etária
  - Estatísticas temporais
  - Exportação para PDF/Excel

### Sistema de Notificações
  - Lembretes de consultas
  - Alertas de idade crítica
  - Comunicação via SMS/email/whatsapp

# 🔒 Cibersegurança - Análise Detalhada
## Vulnerabilidades Identificadas
### v0.0.1
- Armazenamento em Memória: Dados perdidos ao fechar programa
- Validação Limitada: Entradas validadas mas sem sanitização completa
- Sem Logs: Não registra atividades

### v0.0.2
- Persistência Básica: JSON não criptografado
- Sem Autenticação: Acesso livre aos dados
- Serialização JSON: Risco de corrupção de dados

### Recomendações de Melhoria
- Criptografia de Dados
- Validação de Entrada Reforçada
- Sistema de Logs
- Sanitização de JSON
- Controle de Acesso
  - Implementar sistema de usuários
  - Hash de senhas com bcrypt
  - Tokens de sessão

## Medidas Imediatas Recomendadas
  ### Para Produção:
  - Não armazenar em servidor público sem autenticação
  - Implementar HTTPS se transformado em API
  - Backup regular com criptografia

  ### Para Desenvolvimento:
  - Adicionar testes unitários para validações
  - Implementar análise estática de código
  - Revisão de código por pares


*📄 Repositório acadêmico - Desenvolvido para fins educacionais*
