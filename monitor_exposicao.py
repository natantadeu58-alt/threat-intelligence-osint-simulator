import time
from datetime import datetime

BASE_DE_VAZAMENTOS_SIMULADA = {
    "vazamentos": [
        {
            "email": "gerente@globalsecure.com",
            "fonte": "vazamento_forum_Tech_2023",
            "dados_expostos": ["senhas_hash", "usuario"]
        },
        {
            "email": "gerente@globalsecure.com",
            "fonte": "Vazamento_E_commerce_2024",
            "dados_expostos": ["senha_plana", "endereço"]
        },
        {
            "email": "suporte@globalsecure.com",
            "fonte": "Vazamento_Curso_Online_2025",
            "dados_expostos": ["senhas_hash"]
        },
        {
            "email": "dev_estagio@globalsecure.com",
            "fonte": "Github_Public_Secret_Scanning",
            "dados_expostos": ["chave_api_producao"]
        }
    ]
}

def analisar_exposicao_empresa(dominio_alvo):
    print("=" * 70)
    print(f" INICIANDO AUDITORIA DE EXPOSIÇÃO DIGITAL PARA: {dominio_alvo}")
    print(f" Data/Hora da Análise:{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("=" * 70)
    print("[*] Vasculhando fontes públicas e histórico de brechas de dados...")
    time.sleep(1.5)
    total_alertas = 0

    for vazamento in BASE_DE_VAZAMENTOS_SIMULADA["vazamentos"]:
        email_analisado = vazamento["email"]
        if email_analisado.endswith(dominio_alvo):
            total_alertas += 1
            print(f"\n [ALERTA DE RISCO] Exposição detectada para o colaborador!")
            print(f" Email afetado: {email_analisado}")
            print(f" Fonte do vazamento: {vazamento['fonte']}")
            print(f" Dados que vazaram: {', '.join(vazamento['dados_expostos'])}")
            if "chave_api_producao" in vazamento["dados_expostos"]:
                print("[AÇÃO RECOMENDADA]: Revogar a chave API exposta imediatamente no console de nuvem!")
            else:
                print("[AÇÃO RECOMENDADA]: Forçar redefinição de senha e validar ativação de MFA (Duplo Fator).")
            print("-" * 50)

    time.sleep(1)
    print("\n" + "=" * 70)
    print(f" RESUMO DA AUDITORIA:")
    print(f" -> Domínio verificado:{dominio_alvo}")
    print(f" -> Total de credenciais expostas encontradas: {total_alertas}")
    if total_alertas > 0:
        print("STATUS: Risco Identificado. Recomenda-se aplicar o plano de remediação.")
    else:
        print("STATUS: Nenhuma credencial exposta detectada nas fontes públicas simuladas.")
    print("=" * 70)


if __name__ == "__main__":
    dominio_para_auditar = "globalsecure.com"
    analisar_exposicao_empresa(dominio_para_auditar)
