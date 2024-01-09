from fastapi import FastAPI, Form, HTTPException
import pickle
from sklearn.svm import SVC
from fastapi.middleware.cors import CORSMiddleware


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


@app.post("/endpoint")
async def receber_formulario(
        comprimento_sepala: str = Form(...),
        largura_sepala: str = Form(...),
        comprimento_petala: str = Form(...),
        largura_petala: str = Form(...),
):
    
    print("teste")
    
    try:
        X = [comprimento_sepala, largura_sepala, comprimento_petala, largura_petala]

        print(X)

        svm = carregar_modelo_ia()

        predicao = fazer_previsao(svm, X)

        return {"resposta": predicao}

    except Exception as e:
        print(f"Erro: {e}")
        raise HTTPException(status_code=422, detail="Erro de processamento.")


def carregar_modelo_ia():
    
    arquivo = "./iaModel/classificador_svm.sav" 

    classificador_svm = pickle.load(open(arquivo))

    return classificador_svm



def fazer_previsao(svm, X):

    tabela_de_convercao = ["Setosa", "Versicolor", "Virgínica"]
    
    y_pred = svm.predict([X])

    return tabela_de_convercao[y_pred]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)