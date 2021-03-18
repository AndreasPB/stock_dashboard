from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory='src/templates')

@app.get('/')
def dashboard(request: Request):
    """
    Displays the stock dashboard
    """
    return templates.TemplateResponse('dashboard.html',{
        'request': request
    })

@app.post('/stock')
def create_stock():
    """
    Creates a stock and stores it in the db
    """
    return {
        'code': 'success',
        'message': 'stock created'
    }