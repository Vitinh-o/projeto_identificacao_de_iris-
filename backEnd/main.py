from fastapi import FastAPI, Form, HTTPException
import pickle
from sklearn.svm import SVC

app = FastAPI()


@app.post("/receber-form")
async def receber_formulario(
    comprimento_sepala: float = Form(...),
    largura_sepala: float = Form(...),
    comprimento_petala: float = Form(...),
    largura_petala: float = Form(...),
):
    

    X = [comprimento_sepala, largura_sepala, comprimento_petala, largura_petala]

    svm = carregar_modelo_ia()

    predicao = fazer_previsao(svm, X)

    return {"resposta": predicao}



def carregar_modelo_ia():
    
    arquivo = "./iaModel/classificador_svm.sav" 

    classificador_svm = pickle.load(open(arquivo))

    return classificador_svm



def fazer_previsao(svm, X):

    tabela_de_convercao = ["Setosa", "Versicolor", "Virgínica"]
    
    y_pred = svm.predict()

    return tabela_de_convercao[y_pred]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)