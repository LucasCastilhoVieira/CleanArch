from fastapi import APIRouter


router = APIRouter(prefix='/teste')


router.get('/hello')
def read():
    return 'hello'


