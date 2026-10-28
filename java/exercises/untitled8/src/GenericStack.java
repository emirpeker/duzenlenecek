import java.util.ArrayList;

public class GenericStack<E>{
    private ArrayList<E> list=new ArrayList<>();
    
    public int getSize(){
        return list.size();
    }
    public void push(E o){
        list.add(o);
    }
    public E pop(){
        if(list.isEmpty()) return null;
        E o=list.get(getSize()-1);
        list.remove(getSize()-1);
        return o;
    }
}