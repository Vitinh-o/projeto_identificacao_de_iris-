from fastapi import FastAPI, Form, HTTPException
import pickle
from sklearn.svm import SVC

app = FastAPI()


@app.post("/enviar-json")
async def enviar_json(dados_json: dict):
    # Faça algo com os dados JSON recebidos
    # Neste exemplo, apenas os retorna
    return dados_json


@app.post("/receber-form")
async def receber_formulario(
    campo1: str = Form(...),
    campo2: int = Form(...),
    campo3: float = Form(...),
    campo_opcional: str = Form(None),
):
    # Faça algo com os dados do formulário
    # Neste exemplo, apenas os retorna
    return {
        "campo1": campo1,
        "campo2": campo2,
        "campo3": campo3,
        "campo_opcional": campo_opcional,
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)


def carregar_modelo_ia():
    
    arquivo = "./iaModel/classificador_svm.sav" 

    classificador_svm = pickle.load(open(arquivo))

    return classificador_svm



def fazer_previsao(svm, X):

    y_pred = svm.predict()

    return y_pred


svm = carregar_modelo_ia()

