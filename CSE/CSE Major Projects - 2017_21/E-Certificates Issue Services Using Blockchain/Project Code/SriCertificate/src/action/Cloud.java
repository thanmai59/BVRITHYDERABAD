package action;
import java.io.File;
import java.io.FileInputStream;
import org.apache.commons.net.ftp.FTPClient;


public class Cloud {

    FTPClient client = new FTPClient();
    FileInputStream fis = null;
    boolean status;

    public boolean upload(File file,String fname) {
        try {
            client.connect("ftp.drivehq.com");
            client.login("EcertificatesMajorProject", "projectdemo123");
            client.enterLocalPassiveMode();
            fis = new FileInputStream(file);
            
            //status = client.storeFile(" /kk/" +"E:\\sriproj\\SriCertiFicate\\WebRoot\\file\\sindhu.pdf", fis);
            status = client.storeFile("/new/"+ fname, fis);
            client.logout();
            fis.close();

        } catch (Exception e) {
        	e.printStackTrace();
            System.out.println();
        }
        if (status) {
            System.out.println("success");
            return true;
        } else {
            System.out.println("failed");
            return false;
        }
    }
    
 
    public static void main(String args[]){
    	
    boolean f=	new Cloud().upload(new File("E:\\sriproj\\SriCertiFicate\\WebRoot\\file\\sindhu.pdf"),"sindhu");
  System.out.println("=================="+f);
    
    }
    
    
}
