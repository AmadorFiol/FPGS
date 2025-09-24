public class Numero {
    private Integer num=0;

    public Numero(Integer num) {
        this.num=num;
    }
    public void increment() {
        num++;
    }

    public Integer getNum(){
        return num;
    }

    public void setNum(Integer num){
        this.num=num;
    }
}
