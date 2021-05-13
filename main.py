import argparse
import papermill as pm

def main(fechas):
    pm.execute_notebook(
    './entradaFinal.ipynb',
    './out/salidaFinal.ipynb',
    parameters=dict(fecha_inicio=fechas[0],fecha_fin=fechas[1])
    )
    
        
if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument('date',
          help='Fecha Inicial y Fecha Final',
      type=str
    )

    arguments = args.parse_args()
    main([i for i in arguments.date.split(',')])
    
