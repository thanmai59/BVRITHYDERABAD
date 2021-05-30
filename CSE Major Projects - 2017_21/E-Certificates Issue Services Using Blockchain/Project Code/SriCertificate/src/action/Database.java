

package action;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;


public class Database {

    public static Connection getConnection() throws SQLException, ClassNotFoundException, InstantiationException, IllegalAccessException {
        Connection con = null;
        try {
            String url = "jdbc:mysql://localhost:3306/srisindhu";
            String driver = "com.mysql.jdbc.Driver";
            Class.forName(driver).newInstance();
            con = DriverManager.getConnection(url, "root", "root");
            System.out.println("Database Connected Successfully");

        } catch (Exception e) {
            System.out.println("Error in Database" + e.getMessage());
        }
        return con;
    }
    public static void main(String[] agrs) throws ClassNotFoundException, SQLException, InstantiationException, IllegalAccessException
    {
       Database.getConnection();
    }
}
