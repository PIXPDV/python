import requests
import json
import hashlib
import base64
import hmac

BASE_URL = "https://pixpdv.com.br/api/v1"
BASE_URL_HOMOLOGACAO = "https://pixpdv.com.br/api-h/v1"

class PIXPDV:
    def __init__(self, cnpj, token, secret, homologacao=False):
        self.homologacao = homologacao
        self.cnpj = cnpj if homologacao else '00641418000188'
        self.token = token if homologacao else 'tk-ezI0OTgwMzRDLUE1MzctNDM3QS1CQTk0LUZFODlFMEE0MzIyNn0'
        self.secret = secret if homologacao else 'sk-e0JBNTFGRTY0LTczMkYtNDYxNC1CQ0Q1LUI0OTVDODgxOTUwRX0'
        self.session = requests.Session()
        # self.session.headers = {
        #     'Content-Type': 'application/json',
        #     'Authorization': 'Basic ' + base64.b64encode(f"{self.cnpj}:{self.token}".encode()).decode(),
        # }
        self.base_url = BASE_URL if homologacao else BASE_URL_HOMOLOGACAO

    def _gerar_hmac(self, data):
        message = json.dumps(data).encode()
        secret = self.secret.encode()
        hmac_digest = hmac.new(secret, message, digestmod=hashlib.sha256)
        return hmac_digest.hexdigest()

    def statusToken(self):
        body = {'cnpj': self.cnpj}
        try:
            self.session.headers = {
                'Content-Type': 'application/json',
                'Json-Hash': self._gerar_hmac(body),
                'Authorization': 'Basic ' + base64.b64encode(f"{self.cnpj}:{self.token}".encode()).decode(),
            }
            response = self.session.post(f'{self.base_url}/statustoken', json=body)
            data = response.json()
            return data
        except Exception as e:
            return str(e)

    def QRDinamico(self, valor, minutos, msg, imagem=False):
        body = {'valor': valor, 'minutos': minutos, 'mensagem': msg, 'imagem': imagem}
        try:
            self.session.headers = {
                'Content-Type': 'application/json',
                'Json-Hash': self._gerar_hmac(body),
                'Authorization': 'Basic ' + base64.b64encode(f"{self.cnpj}:{self.token}".encode()).decode(),
            }
            response = self.session.post(f'{self.base_url}/qrdinamico', json=body)
            data = response.json()
            return data
        except Exception as e:
            return str(e)

    def QRCobranca(self, valor, vencimento, expira, msg, pagador, juros, multa, desconto, img=False, documento=""):
        body = {
            'valor': valor,
            'vencimento': vencimento,
            'expira': expira,
            'mensagem': msg,
            'imagem': img,
            'documento': documento,
            'pagador': pagador,
            'juros': juros,
            'multa': multa,
            'desconto': desconto
        }
        try:
            self.session.headers = {
                'Content-Type': 'application/json',
                'Json-Hash': self._gerar_hmac(body),
                'Authorization': 'Basic ' + base64.b64encode(f"{self.cnpj}:{self.token}".encode()).decode(),
            }
            response = self.session.post(f'{self.base_url}/qrcobranca', json=body)
            data = response.json()
            return data
        except Exception as e:
            return str(e)
        
    def QRDinamicoRemove(self, qrcodeid):
        try:
            response = self.session.delete(f'{self.base_url}/qrdinamico?qrcodeid={qrcodeid}')
            data = response.json()
            return data
        except Exception as e:
            return str(e)
        
    def QRCobrancaRemove(self, qrcodeid):
        try:
            response = self.session.delete(f'{self.base_url}/qrcobranca?qrcodeid={qrcodeid}')
            data = response.json()
            return data
        except Exception as e:
            return str(e)

    def QRStatus(self, qrcodeid):
        try:
            response = self.session.get(f'{self.base_url}/qrstatus?qrcodeid={qrcodeid}')
            data = response.json()
            return data
        except Exception as e:
            return str(e)

    def QRRefund(self, qrcodeid):
        body = {'qrcodeid': qrcodeid}
        try:
            self.session.headers = {
                'Content-Type': 'application/json',
                'Json-Hash': self._gerar_hmac(body),
                'Authorization': 'Basic ' + base64.b64encode(f"{self.cnpj}:{self.token}".encode()).decode(),
            }
            response = self.session.post(f'{self.base_url}/qrrefund', json=body)
            data = response.json()
            return data
        except Exception as e:
            return str(e)

    def resumo(self, inicio, fim, tipo):
        try:
            response = self.session.get(f'{self.base_url}/qrresumo?inicio={inicio}&fim={fim}&tipo={tipo}')
            data = response.json()
            return data
        except Exception as e:
            return str(e)

    def saldo(self):
        try:
            response = self.session.get(f'{self.base_url}/saldo')
            data = response.json()
            return data
        except Exception as e:
            return str(e)

    def Retirada(self, valor):
        body = {'valor': valor}
        try:
            self.session.headers = {
                'Content-Type': 'application/json',
                'Json-Hash': self._gerar_hmac(body),
                'Authorization': 'Basic ' + base64.b64encode(f"{self.cnpj}:{self.token}".encode()).decode(),
            }
            response = self.session.post(f'{self.base_url}/retirada', json=body)
            data = response.json()
            return data
        except Exception as e:
            return str(e)

    def extrato(self, inicio, fim):
        try:
            response = self.session.get(f'{self.base_url}/extrato?inicio={inicio}&fim={fim}')
            data = response.json()
            return data
        except Exception as e:
            return str(e)
