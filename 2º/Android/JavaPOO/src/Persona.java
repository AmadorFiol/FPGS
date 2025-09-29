public class Persona {
    String nombre;
    Integer edad;
    String dni;
    char sexo;
    Double peso;
    Double altura;

    public Persona(){
        this.nombre="";
        this.edad=0;
        this.dni="";
        this.sexo='H';
        this.peso=0.0;
        this.altura=0.0;
    }

    public Persona(String nombre, Integer edad, char sexo){
        this.nombre=nombre;
        this.edad=edad;
        this.dni="";
        this.sexo=sexo;
        this.peso=0.0;
        this.altura=0.0;
    }

    public Persona(String nombre, Integer edad, String dni, char sexo, Double peso, Double altura){
        this.nombre=nombre;
        this.edad=edad;
        this.dni=dni;
        this.sexo=sexo;
        this.peso=peso;
        this.altura=altura;
    }

    public String getNombre(){
        return this.nombre;
    }

    public void setNombre(String nombre){
        this.nombre=nombre;
    }

    public Integer getEdad(){
        return this.edad;
    }

    public void setEdad(Integer edad){
        this.edad=edad;
    }

    public String getDni(){
        return this.dni;
    }

    public void setDni(String dni){
        this.dni=dni;
    }

    public char getSexo(){
        return this.sexo;
    }

    public void setSexo(char sexo){
        this.sexo=sexo;
    }

    public Double getPeso(){
        return this.peso;
    }

    public void setPeso(Double peso){
        this.peso=peso;
    }

    public Double getAltura(){
        return this.altura;
    }

    public void setAltura(Double altura){
        this.altura=altura;
    }

    public Integer calcularIMC(){
        Double imc = this.peso / Math.pow(this.altura, 2);
        if(imc<20.0){
            return -1;
        } else if (imc>=20.0 && imc<25.0){
            return 0;
        } else if (imc>=25.0){
            return 1;
        }
    }
}
