from flask import request
from database.db import db
from models.stockin import StockIn

def stockin_controller():
    if request.method == 'POST':
        try:
            data = request.get_json()
            print(data)
            stockin = StockIn(data['idProduct'], data['qtt'], data['date'], data['idRequester'])
            db.session.add(stockin)
            db.session.commit()
            return 'StockIn Criado', 201
        except Exception as e:
            return {'error': f'StockIn não criado: {e}'}, 400
    elif request.method == 'GET':
        try:
            data = StockIn.query.all()
            return [si.to_dict() for si in data], 200
        except Exception as e:
            return {'error': f'Erro ao buscar StockIns: {e}'}, 400
    elif request.method == 'PUT':
        try:
            data = request.get_json()
            stockin_id = data['id']
            stockin = StockIn.query.get(stockin_id)
            if stockin is None:
                return {'error': 'StockIn não encontrado'}, 404
            stockin.idProduct = data.get('idProduct', stockin.idProduct)
            stockin.qtt = data.get('qtt', stockin.qtt)
            stockin.date = data.get('date', stockin.date)
            stockin.idRequester = data.get('idRequester', stockin.idRequester)
            db.session.commit()
            return 'StockIn atualizado com sucesso', 200
        except Exception as e:
            return {'error': f'Erro ao atualizar StockIn: {e}'}, 400
    elif request.method == 'DELETE':
        try:
            data = request.get_json()
            stockin_id = data['id']
            stockin = StockIn.query.get(stockin_id)
            if stockin is None:
                return {'error': 'StockIn não encontrado'}, 404
            db.session.delete(stockin)
            db.session.commit()
            return 'StockIn deletado com sucesso', 200
        except Exception as e:
            return {'error': f'Erro ao deletar StockIn: {e}'}, 400
