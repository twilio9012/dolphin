public class linearsearch {
    public static void demo(Integer key){
        System.debug('Linear Search');
        integer s = -1;
        List<integer> lon = new List<integer> ();
        lon.add(3);
        lon.add(4);
        lon.add(5);
        lon.add(6);
        lon.add(7);
        System.debug('List' + lon);
        for(integer i = 0; i < lon.size(); i++){
            if(key == lon[i]){
                s = 1;
            }
        }
        
        if(s == 1){
            System.debug('Element found');
        }
        else{
            System.debug('Element not foud');
        }
    }

}