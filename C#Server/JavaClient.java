import java.io.*;
import java.net.Socket;

public class Client {

    public static void main(String[] args)
    {
        try {
            Socket client = new Socket("127.0.0.1", 5434);
            PrintWriter out = new PrintWriter(new OutputStreamWriter(client.getOutputStream()));
            BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));
            out.print("Hello Server");
            out.flush();
            String message = in.readLine();
            System.out.println(message);
        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
