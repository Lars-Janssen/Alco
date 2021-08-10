/**
 * opg
 */

import java.util.*;

public class opg {
    public static void main(String[] args) {
        ArrayList lijst = new ArrayList<Integer>();
        int n = 3;
        for(int i = 1; i <= n; i++)
        {
            lijst.add(i);
        }
        bereken(lijst);
    }

    static void bereken(ArrayList a)
    {
        if(a.size() > 1)
        {
            for(int i = 0; i < a.size(); i++)
            {
                ArrayList nieuw = new ArrayList<>();
                System.out.print(i);
                //vul nieuw met de dingen van a, maar niet i
                for(int j = 0; j < a.size(); j++) {
                    if(i != j)
                    {
                        nieuw.add(a.get(j));
                    }
                }
                bereken(nieuw);
            }
        }
        else
        {
            System.out.print(a.get(0));
        }
    }
}