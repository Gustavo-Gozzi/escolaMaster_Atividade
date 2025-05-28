import requests
import unittest
from time import sleep

class TestStringMethods(unittest.TestCase):
    def test_001_POST_Atividade(self):
        r = requests.post("http://127.0.0.1:8880/atividade", json = {
            "dt_entrega": "31-12-2026",
            "materia": "Ressuticação",
            "professor_id": 1,
            "turma_id": 1 
        })
        self.assertEqual(r.status_code, 200)

        rec = False
        resposta = requests.get("http://127.0.0.1:8880/atividade")
        atividades = resposta.json()
        for atividade in atividades:
            if atividade["materia"] == 'Ressuticação':
                rec = True
        
        if not rec:
            self.fail("Atividade não encontrada.")
             


    def test_002_GET_Atividade(self):
        resposta = requests.get("http://127.0.0.1:8880/atividade")
        atividades = resposta.json()

        rec = False
        for atividade in atividades:
            if atividade["materia"] == 'Ressuticação':
                rec = True
        
        if not rec:
            self.fail("Atividade não encontrada.")

    
    def test_003_DELETE_Atividade(self):
        resposta = requests.get("http://127.0.0.1:8880/atividade")
        self.assertEqual(resposta.status_code, 200)
        atividades = resposta.json()

        for atividade in atividades:
            print(atividade)
            if atividade["materia"] == 'Ressuticação':
                ide = atividade["id"]
                resp = requests.delete(f"http://127.0.0.1:8880/atividade/{ide}")
                self.assertEqual(resp.status_code, 200)
                
    
        resp = requests.get("http://127.0.0.1:8880/atividade")
        atctivitys = resp.json()

        rec = False
        for activity in atctivitys:
            if activity["materia"] == 'Ressucitação':
                rec = True
        
        if rec:
            self.fail("Atividade não foi deletada!")


        



def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    runTests()