import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

 class TestServer {
    public static void main(String[] args)
    {
        System.out.println("Hello World");
        try {
            ServerSocket server = new ServerSocket(5434);
            Socket aClient =  server.accept();
            System.out.println("Connected");
            PrintWriter out = new PrintWriter(new BufferedOutputStream(aClient.getOutputStream()));
            out.print("Hello!!!!");
            out.flush();
            BufferedReader in = new BufferedReader(new InputStreamReader(aClient.getInputStream()));
            String input = in.readLine();
            System.out.println(input);

            in.close();
            out.close();
            aClient.close();
            server.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
