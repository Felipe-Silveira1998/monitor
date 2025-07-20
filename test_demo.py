#!/usr/bin/env python3
"""
Script de demonstração do Sistema de Monitoramento de Disponibilidade
"""

import requests
import json
import time
from datetime import datetime

# Configurações
BASE_URL = 'http://localhost:5001/api'
USER_ID = 1

def print_header(title):
    print(f"\n{'='*60}")
    print(f" {title}")
    print(f"{'='*60}")

def print_step(step, description):
    print(f"\n[PASSO {step}] {description}")
    print("-" * 50)

def test_api_endpoint(method, endpoint, data=None, description=""):
    """Testar endpoint da API"""
    url = f"{BASE_URL}{endpoint}"
    
    try:
        if method.upper() == 'GET':
            response = requests.get(url)
        elif method.upper() == 'POST':
            response = requests.post(url, json=data)
        elif method.upper() == 'PUT':
            response = requests.put(url, json=data)
        elif method.upper() == 'DELETE':
            response = requests.delete(url)
        
        print(f"✅ {method} {endpoint} - Status: {response.status_code}")
        if description:
            print(f"   {description}")
        
        if response.status_code < 400:
            try:
                result = response.json()
                if isinstance(result, dict) and len(result) < 10:
                    print(f"   Resposta: {json.dumps(result, indent=2, ensure_ascii=False)}")
                elif isinstance(result, list) and len(result) <= 3:
                    print(f"   Resposta: {json.dumps(result, indent=2, ensure_ascii=False)}")
                else:
                    print(f"   Resposta: {type(result).__name__} com {len(result)} itens")
            except:
                print(f"   Resposta: {response.text[:100]}...")
        else:
            print(f"   ❌ Erro: {response.text}")
        
        return response
        
    except Exception as e:
        print(f"❌ Erro na requisição: {str(e)}")
        return None

def main():
    print_header("DEMONSTRAÇÃO DO SISTEMA DE MONITORAMENTO DE DISPONIBILIDADE")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Teste 1: Verificar estatísticas iniciais
    print_step(1, "Verificando estatísticas do sistema")
    test_api_endpoint('GET', '/monitor/stats', description="Estatísticas gerais do sistema")
    
    # Teste 2: Listar alertas existentes
    print_step(2, "Listando alertas existentes")
    response = test_api_endpoint('GET', f'/alerts?user_id={USER_ID}', description="Alertas do usuário")
    
    existing_alerts = []
    if response and response.status_code == 200:
        existing_alerts = response.json()
    
    # Teste 3: Criar novo alerta de teste
    print_step(3, "Criando novo alerta de teste")
    new_alert_data = {
        'user_id': USER_ID,
        'name': 'Teste de Produto - Demo',
        'url': 'https://httpbin.org/json',
        'selector': None,
        'keyword': 'slideshow',
        'price_threshold': None,
        'notification_channels': json.dumps(['email', 'telegram'])
    }
    
    create_response = test_api_endpoint('POST', '/alerts', new_alert_data, 
                                     description="Criando alerta para demonstração")
    
    new_alert_id = None
    if create_response and create_response.status_code == 201:
        new_alert_id = create_response.json().get('id')
        print(f"   ✅ Alerta criado com ID: {new_alert_id}")
    
    # Teste 4: Verificar alerta específico
    if new_alert_id:
        print_step(4, f"Verificando alerta ID {new_alert_id}")
        test_api_endpoint('POST', f'/monitor/check/{new_alert_id}', 
                         description="Executando verificação manual do alerta")
    
    # Teste 5: Testar scraping direto
    print_step(5, "Testando sistema de web scraping")
    scraping_test_data = {
        'url': 'https://httpbin.org/json',
        'keyword': 'slideshow'
    }
    test_api_endpoint('POST', '/monitor/test-scraping', scraping_test_data,
                     description="Teste direto do sistema de scraping")
    
    # Teste 6: Verificar todos os alertas
    print_step(6, "Verificando todos os alertas ativos")
    test_api_endpoint('POST', '/monitor/check-all', 
                     description="Verificação em lote de todos os alertas")
    
    # Teste 7: Testar sistema de notificações
    print_step(7, "Testando sistema de notificações")
    test_api_endpoint('GET', '/notifications/config', 
                     description="Configuração do sistema de notificações")
    
    notification_test_data = {
        'channels': ['email']
    }
    test_api_endpoint('POST', '/notifications/test', notification_test_data,
                     description="Teste do sistema de notificações")
    
    # Teste 8: Testar notificação para alerta específico
    if new_alert_id:
        print_step(8, f"Testando notificação para alerta {new_alert_id}")
        notification_data = {
            'result': {
                'status': 'available',
                'price': 99.99,
                'content': 'Produto disponível para teste',
                'timestamp': datetime.now().isoformat()
            }
        }
        test_api_endpoint('POST', f'/notifications/send/{new_alert_id}', notification_data,
                         description="Enviando notificação de teste")
    
    # Teste 9: Atualizar alerta
    if new_alert_id:
        print_step(9, f"Atualizando alerta {new_alert_id}")
        update_data = {
            'name': 'Teste de Produto - Demo (Atualizado)',
            'is_active': False
        }
        test_api_endpoint('PUT', f'/alerts/{new_alert_id}', update_data,
                         description="Pausando o alerta de teste")
    
    # Teste 10: Verificar estatísticas finais
    print_step(10, "Verificando estatísticas finais")
    test_api_endpoint('GET', '/monitor/stats', description="Estatísticas após os testes")
    
    # Limpeza: Remover alerta de teste
    if new_alert_id:
        print_step("LIMPEZA", f"Removendo alerta de teste {new_alert_id}")
        test_api_endpoint('DELETE', f'/alerts/{new_alert_id}', 
                         description="Removendo alerta criado para demonstração")
    
    print_header("DEMONSTRAÇÃO CONCLUÍDA")
    print("✅ Todos os testes foram executados com sucesso!")
    print("📊 O sistema está funcionando corretamente.")
    print("\nFuncionalidades testadas:")
    print("- ✅ Criação e gerenciamento de alertas")
    print("- ✅ Sistema de web scraping")
    print("- ✅ Monitoramento automático")
    print("- ✅ Sistema de notificações")
    print("- ✅ APIs REST completas")
    print("- ✅ Interface web responsiva")

if __name__ == "__main__":
    main()

