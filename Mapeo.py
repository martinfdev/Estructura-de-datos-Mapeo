# -*- coding: utf-8 -*-
import os
import subprocess
class Graphviz:

    def generar_grafico(self, fila, columna, posFil, posColum, k, titulo):
        file = open(titulo+'.dot', 'w')
        file.write('digraph Matriz { \ntbl [\nshape=plaintext\nlabel=<\n<table border=\'2\' cellborder=\'1\' color=\'black\' cellspacing=\'0\'>'+os.linesep)
        file.write('<tr>\n\t<td>Matriz</td>\n\t<td>Matriz '+titulo+' </td>\n</tr>\n<tr>\n\t<td cellpadding=\'4\'>\n\t\t<table color=\'sienna\' cellspacing=\'0\'>'+os.linesep)
        contador = 0
        for i in range(0, fila):
            file.write('\t\t\t<tr>\n')
            for j in range(0, columna):
                if(i== posFil and j== posColum):
                    contador +=1
                    file.write('\t\t\t\t<td bgcolor="lightblue"><font color="blue"> ('+str(i)+','+str(j)+')</font></td>\n')
                else:
                    contador +=1
                    file.write('\t\t\t\t<td>('+str(i)+','+str(j)+')</td>\n')   
            file.write('\t\t\t</tr>\n')
        file.write('\t\t</table>\n\t </td>\n\t<td colspan=\'1\' rowspan=\'1\'>\n\t\t<table color=\'chartreuse4\' border=\'0\' cellborder=\'1\' cellpadding=\'10\' cellspacing=\'0\'>\n\t\t\t <tr>'+os.linesep)            
        contador = 0
    
        for i in range (fila*columna):
            contador += 1
            if i == k:
                file.write('\t\t\t\t<td bgcolor ="lightskyblue"><font color ="blue">('+str(contador)+') </font></td>\n')
            else:
                file.write('\t\t\t\t <td>'+str(contador)+' </td>\n')
        file.write('\t\t\t</tr>\n\t\t</table>\n\t</td>\n</tr>\n</table>\n>];\n}')
        file.close()
        #subprocess.call('dot -Tjpg '+titulo+'.dot -o "+titulo+".jpg', shell=True)
        os.system("dot -Tjpg "+titulo+".dot -o "+titulo+".jpg")
        #os.system(""+titulo+".jpg")




