import random

llave_oxidada = False
escaleras = []
clave_justos = []

welcome = "Bien llegado buscador. ¿Eres capaz de escapar?"
print("\n"+welcome+"\n"+"*"*len(welcome)+"\n")
print("""Te has despertado, es un lugar oscuro; techo, piso y paredes de roca.
Miras alrededor, una vez te acostumbras a la poca luz puedes ver que tras de
ti hay una ventana con dos barrotes rotos y a tu derecha una puerta, de lo 
que ahora reconoces como una jaula, está bierta.
      """)

pregunta_1 = input("¿Qué escoges para salir de la celda?\n"
                    "A- Puerta abierta\n"
                    "B- Ventana rota\n")

print("""Antes de ponerte en marcha te tropiezas con un pequeño objeto. Al bajar la 
vista notas que es una vieja, rustica y oxidada llave.
Esta llave está maldita por los que vinieron antes que tú, cada paso que des la hará más pezada
y cada duda que albergues en tu corazón retumbara en su acero que hará de faro para las bestias 
que buscan saciarse con la carne fresa de quien sale de la celda.
      """)

pregunta_2 = input("¿Recoges la llave?\n"
                    "A- Si\n"
                    "B- No\n")

if pregunta_2 == "A":
      llave_oxidada = True
else:
      llave_oxidada = False

if pregunta_1 == "A":
      
      print("""\nCaminas por un largo pasillo y tras varios metros te topas con un mensaje
escrito en las paredes:
**El destino de los justos encegece a los condenados**
Sería sabio guardar el mensaje en la mente.
            """)
      
      print("""Un poco más de luz comienza a colarse por algún lugar del pasillo,
das unos pasos más y el humedo sonido de tus pisadas sobre un líquido oscuro
es la primera alerta de lo que te encontraras a continuación. El oscuto líquido del 
charco es sangre y al doblar la esquina del pasillo encuentras el cuerpo del 
que proviene.
            """)
      
      pregunta_3 = input("Una mujer muy mal herida extiende su mano pidiendote ayuda\n"
                  "¿Le brindas ayuda a la mujer?\n"
                    "A- Si\n"
                    "B- No\n")
      
      if pregunta_3 == "A":
            
          print("""\nTe agachas a constatar el estado de la mujer. Ella al sentirte cerca
se abalanza a ti y se aferra a tu cuerpo con sus 
ultimas fuerzas.
                """)
          
          pregunta_4 = input("Con un hilo de voz la mujer susurra en tu oido:\n"
                  "Mis pecados han sido más grandes que los tuyos\n"
                  "¿De los dos quién debería tomar el castigo?\n"
                    "A- Tomas el castigo por la mujer\n"
                    "B- Rechazas ser castigado\n")
          
          if pregunta_4 == "A" and llave_oxidada == True:
                
                  print("""\nLa mujer se aleja y ves que en su mano está la llave oxidada,
sin decir una palabra más, ves como aquel cuerpo herido como última acción
introduce la llave en su ojo derecho, vaciando la cuenca.
Cuando la vida abandona el cuerpo de la mujer, la sangre dibuja en una de
las paredes una puerta, la llave gira y la puerta es abierta.
Felicidades buscador. Toma la llave, el objeto es tuyo.
                    """)
                  
          elif pregunta_4 == "A" and llave_oxidada == False:
                
                  print("""En algún momento del cual no te diste cuenta, como si
nunca hubiese pasado, la mujer recobra la belleza perdida, sin ningun rastro
de haber sido agredida. Se funde en un beso contigo.
Estás encerrado en la misma jaula, donde antes habían salidas ahora
son grandes cristales que te muestran lo que la mujer ve.
                        """)
                  
          else:
                
                print("""\nTu fuerza no es suficiente para alejar a la mujer de ti, su 
cuerpo parece volverse más liviano. Repentinamente la mujer se vuelve
una densa y maloliente niebla que viaja hacia tus pulmones.
El respirar la niebla fue tu ultimo acto en vida buscador, ahora
deberas esperar, en eterno dolor, como lo hizo la mujer hasta 
que alguien más vengay te ofrezca la llave.
                        """) 
                 
      if pregunta_3 == "B":
            
          print("""\nCierras los puños y apartas la mirada. Caminas con decisión ignorando
a la moribunda cuyos gritos y sollozos inundan el espacio hasta parecer 
que están apunto de quebrar tu cordura 
            """)
          
          print("""Tras vagabundear por lo que podría ser varias horas terminas el pie
de una escalera. Al pisar cada peldaño un número resuena en tu mente 
conjunto a la siguiente frase:
**Sólo aquellos que han decidido caminar en parejas sin dejar nadie
atras son los que tendrán el camino libre.**
Los número de los seis escalones son:
                """)
          
          for i in range(0,6):
                peldaño = random.randint(0,9)
                print("{}º Peldaño: {}".format((i+1),peldaño))
                if peldaño % 2 == 0:
                      escaleras.append(int(peldaño))
                      
          print("""\nAl subir la escalera una puerta sin cerradura obstruye tu avance.
Un pedazo de piel recién desollada y una barra de hierro al rojo vivo
cuelgan de la puerta. Ahora es cuando debes escribir los números 
asociados a los peldaños de los justos.
                """)
          for i in range(len(escaleras)):
                pregunta_5 = int(input("{}º cifra: ".format(i+1)))
                clave_justos.append(pregunta_5)
          
          #print("clave justos: ",clave_justos)                
          #print("escaleras: ",escaleras)
          
          if clave_justos == escaleras and llave_oxidada == True:
                
                print("""\nTu orientación te ha servido satisfactoriamente buscador.
Ahora puedes marcharte con uno de los objetos que Él tanto 
desea.
                            """)
                
          else:
                
                print("""\nEl pedazo de piel cobra vida y se expande hasta cubrir toda la puerta,
lo que antes era un objeto inanimado se transforma en un avejentado 
y deformado rostro, este te mira con asco y antes de que puedas reaccionar
te baña en un vomito aceitoso. La sustancia toca la barra al rojo 
vivo y te prendes fuego al instante.
Has fallado buscador y antes de que te consumas por completo te arrancare
algo de piel para reemplazar la oportunidad que desperdiciaste.
                            """)
          


if pregunta_1 == "B":
      print("""\n Hay más luz de la que esperarias para estar en medio de la noche, a tu alrededor 
hay decenas de robustos y altos arboles, su tamaño y densidad te hacen intuir que
el bosque nació varios siglos atras. Al alzar la vista, justo encima de tu cabeza
se alzan tres lunas gibosas que gobiernan una boveda celeste carente de estrellas.
""")
      print("""\n Los arboles han crecido tan cerca unos de otros que han dejado sólo
un caminino posible que seguir. Es un camino de tierra hecho por el andar 
de muchos otros que estuvieron en tu lugar. Un tiempo después de seguir aquel camino
das con una bifurcación.
""")
      
      pregunta_6 = input("A tu derecha nace un camino de piedra y a tu izquierda si fuerzas la \n"
                         "vista veras la orilla de un lago de aguas tranquilas.\n"
                         "¿Qué camino tomaras?\n"
                         "A- Sendero de piedra\n"
                         "B- Ir al lago\n")
      
      if pregunta_6 == 'A':
            print("""\nLa noche es agradable, no hay corrientes de aire que puedan causarte
suficiente frio como para incomodarte. Sin embargo, empiezas a notar
la presencia de un manto blanco sobre las ramas de los arboles.
Cuanto más avances más denso es este manto, al principio y a la distancia lo
juzgaste como nieve, pero ahora que practicamente es un velo frente a ti
caes en cuenta que es tela de araña.
""")
            pregunta_7 = input("El espeso telón frente a ti sería perfecto si no tuviera \n"
                               "un bulto a la altura de tu cintura que te recuerda al pomo\n"
                               "de una cerradura\n"
                              "¿Giras el pomo de la cerradura o regresas por el camino andado?\n"
                              "A- Girar pomo\n"
                              "B- Regresar\n") 
            
            if pregunta_6 == 'A' and llave_oxidada == True:
                  print("""\nSe oye el mecánismo de una cerradura activarse, la llave en tu 
bolsillo, sientes el aroma de tu hogar cobrar intensidad. 
Inesperadamente todo queda en silencio, escuchas cientos de ramas crujiendo, 
un leve csoquilleo sobre tu cabeza y hombros. Te percatas demasiado tarde 
que ese cosquilleo proviene de miles de arañas que han descendido de los árboles
que recorren tu cuerpo hasta reclamar un lugar que morder. El veneno
inunda tus venas y sucumbes en medio de espasmos agónicos.
Lo siento buscador. Los caminos del gusano son diferentes a los de la araña.
""")
            else: 
                  print("""\nSe oye el mecánismo de una cerradura activarse, la llave en tu 
bolsillo, sientes el aroma de tu hogar cobrar intensidad. 
El telón tejido por la araña cede y te permite avanzar, el llamdo de tu
hogar es tan grande que apuras el paso pero el camino no parece terminar.
Has estado recorriendolo por días y ahora que casi todas tus fuerzas te han
abandonado, tu hogar se vuelve un espejismo delirante.
Totalmente exhausto sucumbes en medio del camino y la noche interminable, 
te desmayas y al volver abrir los ojos has sido devuelto a la celda donde 
iniciaste, pero tu cuerpo ahora no es más que un conjunto de carne supurante
más cerca del gusano que del hombre.
 Lo siento buscador. Los caminos del gusano son diferentes a los de la araña.
""")
      
      
      if pregunta_6 == 'B':
            print("""\nSigues tu camino hacia el lago, no hay un solo movimiento en él.
Está tan inmovil que se ha vuelto la superficie de un cristal. A la izquierda
siguiendo la orilla del lago te encuentras un muelle y a este un bote de remos 
amarrado.
""")
            
            pregunta_8 = input("Es un bote viejo y en su madera hay evidencias de humedad  \n"
                               "y polillas. La madera se astilla en los bordes.\n"
                              "¿Navegaras en el bote?\n"
                              "A- Si\n"
                              "B- No\n") 
            
            if pregunta_8 == "A":
                  print("""\n Te impulsas con los remos y navegas hasta el centro del lago.
Las tres enloquecedoras lunas se reflejan en la superficie del agua,
el bote a pesar del impulso se detiene en el centro exacto del triángulo
que forman las lunas.
Un pedazo de la apolillada madera cae y deja al descubierto un agujero
que no es más que el hoyo de una cerradura.
""")
                  
                  pregunta_9 = input("Aquellas lunas son juez, jurado y condenado de todo lo que ves  \n"
                               "La llave ayudara a liberarlas y con ellas la enfermedad que cargan.\n"
                              "¿Harás lo que se te demanda?\n"
                              "A- Si\n"
                              "B- No\n")
                  
                  print("""\nUna mancha negra nacida del centro de dos de los tres reflejos 
de las lunas forman números en su superficie. El viento canta el 
siguiente mensaje:
**Cuando la primera y segunda luna propagaron su fuerza, la tercera luna
respondio al llamado mostrando aquello que sus hermanas crearon**
""")
                  
                  luna_1 = random.randint(1,15)
                  luna_2 = random.randint(1,15)
                  luna_3 = luna_1 * luna_2
                  
                  print("{} es la cifra con la que nacio la primera hermana.".format(luna_1))
                  print("{} es la cifra con la que nacio la segunda hermana.".format(luna_2))
                  
                  pregunta_10 = int(input("Buscador danos tu respuesta\n"
                                          "¿Cúal es la cifra de la tercera hermana?\n"))
                  
                  if pregunta_9 == "A":
                        if luna_3 == pregunta_10 and llave_oxidada == True:
                              print("""El lago se congela, un ruido ensordecedor nace del bosque a tu alrededor,
es el grito agónico de todos los que fallaron antes de ti.
Una luz proveniente del horizonte te indicará el camino.
Felicidades buscador, ahora el objeto es tuyo. Sigue tu camino de pena
y agonía.... Tienes mi bendición.
""")
                        else:
                              print("""\nEl dicho de que la ignorancia es atrevida no puede estar más en lo correcto.
Aunque por tu esfuerzo y deboción a las lunas madre, se te ha otorgado 
una oportunidad más.
Del oscuro e infinito cielo nacen miles de extremidades tentaculares que te
toman y elevan hacia el vacio. Cuando tu cordura se agota te desmayas.
Has de despertar en la celda donde iniciaste tu camino, pero los errores tienen un
precio buscador.
Tus ojos, el sentido de la vista es el precio a pagar.
Buena suerte haciendo el camino a ciegas.
""")
                  
                  else:
                        print("""Tu cobardia e ignorancia es avergonzante buscador.
Ahora siente el frío abrazo de las aguas, sentiras la asfixia por una eternidad
sin que se te permita morir o hacer algo para ponerle fin.
""")
                  
            
            else:
                  print("""\nEl piso sobre el que te encuentras se vuelva una pasta grumosa,
su centro te absorbe y cualquier esfuerzo por escapar no hará más que hundirte
con mayor rapidez.
Mi querido buscador, aquellos que no están dispuestos ha subyugarse a las 
guardianas de la boveda celeste no se merecen avanzar de este punto.
""")