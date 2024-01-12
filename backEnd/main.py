from fastapi import FastAPI, Form, HTTPException
import pickle
from sklearn.svm import SVC
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel



app = FastAPI()

origins = [
    "http://localhost",
    "http://127.0.0.1:5500/frontEnd/"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Formulario(BaseModel):

    comprimento_sepala: str
    largura_sepala: str
    comprimento_petala: str
    largura_petala: str



@app.post("/endpoint")
async def receber_formulario(form: Formulario):
        
    try:
        X = [float(form.comprimento_sepala),
        float(form.largura_sepala),
        float(form.comprimento_petala),
        float(form.largura_petala)]

        svm = carregar_modelo_ia()


        predicao = fazer_previsao(svm, X)

        

        return {"resposta": predicao}

    except Exception as e:
        print(f"Erro: {e}")
        raise HTTPException(status_code=422, detail="Erro de processamento.")


def carregar_modelo_ia():
    
    caminho_arquivo = "backEnd\iaModel\classificador_svm.sav" 


    with open(caminho_arquivo, 'rb') as arquivo:
        classificador_svm = pickle.load(arquivo)
    

    return classificador_svm



def fazer_previsao(svm, X):

    tabela_de_convercao = ["Setosa", "Versicolor", "Virgínica"]
    
    y_pred = svm.predict([X])


    return tabela_de_convercao[int(y_pred)]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)