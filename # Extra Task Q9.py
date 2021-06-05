# Extra Task Q9

inp_str = "consultadd"
  

out = {x : inp_str.count(x) for x in set(inp_str )} 
  

print ("Occurrence of all characters in consultadd is :\n "+ str(out))