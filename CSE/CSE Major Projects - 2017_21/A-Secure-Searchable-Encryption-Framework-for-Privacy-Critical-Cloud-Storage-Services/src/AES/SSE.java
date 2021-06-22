package sse;


import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.security.spec.InvalidKeySpecException;


public class SSE {


    public static byte[] xorTwoByteArrays(byte[] byteArray1, byte[] byteArray2) {
        int maxLength = byteArray1.length > byteArray2.length ? byteArray1.length : byteArray2.length;
        int minLength = byteArray1.length > byteArray2.length ? byteArray2.length : byteArray1.length;

        byte[] xorBytes = new byte[maxLength];
        for (int i = 0; i < minLength ; i++){
            xorBytes[i] = (byte) (byteArray1[i] ^ byteArray2[i]);
        }
        if (maxLength == byteArray1.length)
            System.arraycopy(byteArray1,minLength,xorBytes,minLength,maxLength-minLength);
        if (maxLength == byteArray2.length)
            System.arraycopy(byteArray2,minLength,xorBytes,minLength,maxLength-minLength);

        return xorBytes;
    }

    public static byte[] getRandomBytes(int count) {

        // Generate the Salt
        SecureRandom random = new SecureRandom();
        byte[] saltyBytes = new byte[count];
        random.nextBytes(saltyBytes);

        return saltyBytes;
    }
    public static SecretKeySpec getSecretKeySpec(String password, byte[] saltyBytes) throws NoSuchAlgorithmException, InvalidKeySpecException {
        int pswdIterations = 65536;
        int keySize = 128;

        // Derive the key
        SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA1");
        PBEKeySpec spec =  new PBEKeySpec( password.toCharArray(),saltyBytes,
                pswdIterations, keySize );


        SecretKey secretKey = factory.generateSecret(spec);

        return new SecretKeySpec(secretKey.getEncoded(), "AES");
    }

}
