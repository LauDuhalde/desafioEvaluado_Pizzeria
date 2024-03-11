import ingredientes
#Se crea clase sin constructor según ppts
class Pizza:
    tamanio = "Familiar"
    precio = 10000
    
    @staticmethod
    def validar_eleccion(elemento, opciones):
        """
        Valida que el elemento escogido esté dentro de las opciones permitidas.
        ------------
        Parameter
        ------------
        elemento
            Type: String
            Ejemplo:    '1'
        opciones
            Type:   Diccionario
            Ejemplo:    {1:'tomate', 2:'aceitunas', 3:'champiñones'}
        Return
        ------------
        eleccion
            Type:   Boolean
            Descripción:    Indica si elemento es valido (True) o no (False)
        """
        if elemento not in opciones:
            eleccion = False
        else:
            eleccion = True
            
        return eleccion
    
    def realizar_pedido(self):
        """
        Solicita selección de ingredientes y valida que Pizza sea correcta
        ------------
        Parameter
        ------------
        None
        
        Return
        ------------
        None
        """
        self.proteina = input('''Seleccione la proteina:
1. Pollo
2. Vacuno
3. Carne vegetal
>>>\n''')
        self.vegetales = []
        for i in range(2):
            self.vegetales.append(input('''Seleccione la vegetales:
1. Tomate
2. Aceitunas
3. Champiñones
>>>\n'''))
        
        self.tipo_masa = input('''Seleccione el tipo de masa:
1. Tradicional
2. Delgada
>>>\n''')
        self.valida = True
        #Ifs anidados para no evaluar todos los ingredientes en caso de que uno sea inválido
        if not Pizza.validar_eleccion(self.proteina, ingredientes.proteinas):
            self.valida = False
        else:
            for vegetal in self.vegetales:
                #cualquiera de los ingredientes incorrecto hace a la pizza inválida
                if not Pizza.validar_eleccion(vegetal, ingredientes.vegetales): 
                    self.valida = False
            if self.valida:
                if not Pizza.validar_eleccion(self.tipo_masa, ingredientes.tipo_masa):
                    self.valida = False
        
        
        
        