# Relatório de Auditoria de Segurança: Exposição Digital e Credenciais

**Alvo da Auditoria:** GlobalSecure Tech (Ambiente de Simulação Controlado)  
**Data da Auditoria:** Junho de 2026

---

## 1. Sumário Executivo
Este relatório apresenta os resultados da análise de superfície de ataque externa realizada no ambiente simulado da GlobalSecure Tech. O objetivo foi aplicar princípios de engenharia de software voltados para a automação de defesa, identificando possíveis e-mails corporativos e credenciais associadas expostas publicamente na internet, mitigando riscos de vazamento de dados em conformidade com as boas práticas de governança e DevSecOps.

## 2. Metodologia (OSINT)
A investigação foi conduzida de forma passiva através de um script automatizado em Python, projetado com foco em modularidade, tratamento de exceções e consumo limpo de APIs de inteligência de ameaças públicas. Não foram realizados ataques direcionados, testes de intrusão ativos ou invasões a servidores.

## 3. Vulnerabilidades Identificadas
* **ID:** SEC-01
* **Falha:** Exposição de Credenciais Corporativas em Fontes Públicas.
* **Gravidade:** Alta
* **Descrição:** O sistema de monitoramento automatizado detectou que e-mails com o domínio `@globalsecure.com` constavam em bases de dados de vazamentos antigos de terceiros (ex: vazamentos históricos de plataformas de fóruns ou cursos onde os colaboradores usaram o e-mail do trabalho).

## 4. Prova de Conceito (PoC)
O script `monitor_exposicao.py` foi executado apontando para a base de simulação e retornou o seguinte alerta de log estruturado:

```text
[ALERTA] - O e-mail 'gerente@globalsecure.com' foi encontrado em 2 vazamentos públicos!
[AÇÃO RECOMENDADA] Forçar a troca de senha imediatamente.
```

## 5. Plano de Remediação Técnica (Visão de Engenharia)
* **Revogação de Sessões:** Invalidar imediatamente todos os tokens de acesso ativos do usuário `gerente@globalsecure.com` na camada de aplicação.
* **Reset de Senha Forçado:** Exigir a alteração da senha corporativa no próximo login através do Provedor de Identidade (IdP).
* **Implementação de MFA Rígido:** Validar a obrigatoriedade de Segundo Fator de Autenticação (MFA) baseado em push ou FIDO2 para todos os acessos externos.
* **Segurança no Pipeline (DevSecOps):** Integrar a lógica do script `monitor_exposicao.py` a uma esteira de monitoramento contínuo para detectar novas exposições de forma proativa.

## 6. Objetivos de Aprendizado e Conclusão
Como futuro especialista em segurança, o desenvolvimento e a execução desta auditoria simulada permitiram consolidar conceitos práticos de proteção de identidade digital, manipulação segura de APIs de terceiros e mitigação de ataques de *Credential Stuffing*. A correção imediata do vetor SEC-01 eleva a postura de segurança da organização e protege o perímetro contra acessos não autorizados.

---

**Responsável:**  
Natan  
*Estudante de Engenharia de Software*  
*Futuro Especialista e Engenheiro de Segurança Cibernética*

