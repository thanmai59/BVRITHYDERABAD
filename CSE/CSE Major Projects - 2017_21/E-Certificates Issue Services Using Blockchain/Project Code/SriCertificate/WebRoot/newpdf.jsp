<%@ page  import="java.sql.*" import="action.*" %>
<%@ page import="com.lowagie.text.*" %>
<%@ page import="com.lowagie.text.pdf.*" %>
<%@ page import="com.lowagie.text.pdf.draw.LineSeparator" %>
<%@ page import="com.lowagie.text.pdf.PdfPTable" %>
<%@ page import="java.text.SimpleDateFormat" %>
<%@ page import="java.io.*,java.util.*,java.sql.*,action.*"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>

<%
Connection con = null;
ResultSet rs=null;
PreparedStatement stmt = null;

        try {
            String id= session.getAttribute("v").toString();;
  System.out.println("id is download"+id);
  String n = session.getAttribute("n1").toString();
  System.out.println("name is"+n);
String filename = "sri" + n + ".pdf";
  String Content1=null,Content2=null,Content3=null,Content4=null,Content5=null,Content6=null,Content7=null,Content8=null,Content9=null;
  con =Database.getConnection();
Statement stm=con.createStatement();
stmt=con.prepareStatement("select * from StudentRecLetter  where  emailid=?");
        stmt.setString(1,id);
        ResultSet rst = stmt.executeQuery();
        if (rst.next())
        {
            
            
            
         
            Content3 = rst.getString("rollno");
            Content2 = rst.getString("name");
             Content1 = rst.getString("emailid");
            Content4 = rst.getString("usertype");
            Content5 = rst.getString("cname");
            Content6 = rst.getString("Description");
           // Content7 = rst.getString("purpose");
           // Content8 = rst.getString("pic");
           // Content9 = rst.getString("email");
            
        }

           String total = null;
        String file = null;
        
            file = "E:\\sripp\\RecLeter.pdf";
        
       
            Document document = new Document(PageSize.A4);
            PdfWriter writer = PdfWriter.getInstance(document, new FileOutputStream(new File(file)));
            document.open();/////////////////////////////////
            
            ////////////////////////////////////////////////
            PdfPTable table6 = new PdfPTable(2);
            table6.setWidthPercentage(81);

            table6.getDefaultCell().setBorder(PdfPCell.NO_BORDER);

            Font fontbold = FontFactory.getFont("Times-Roman", 15, Font.BOLD);
            Font font = FontFactory.getFont("Times-Roman", 12, Font.BOLD);
           // Image image1 = Image.getInstance("E:\\sripp\\SriImage.jpg");
          // PdfPTable nested = new PdfPTable(1);
          // nested.getDefaultCell().setBorder(PdfPCell.NO_BORDER);
           // nested.addCell(image1);

           // table6.addCell(nested);
            PdfPTable nested1 = new PdfPTable(1);
            nested1.getDefaultCell().setBorder(PdfPCell.NO_BORDER);
            nested1.getDefaultCell().setHorizontalAlignment(Element.ALIGN_CENTER);

            nested1.addCell(new Phrase("BVRIT  ENGINEERING(AUTONOMOUS) Hyderabad", FontFactory.getFont("Times-Roman", 15, Font.BOLD)));
              Image image1 = Image.getInstance("E:\\sripp\\sriGVP.jpg");
           PdfPTable nested = new PdfPTable(1);
           nested.getDefaultCell().setBorder(PdfPCell.NO_BORDER);
            nested1.addCell(new Phrase("", font));
           table6.addCell(nested);
         nested1.addCell(new Phrase("", font));
           table6.addCell(nested1);
            float[] columnWidths1 = new float[]{10f, 80f};
            table6.setWidths(columnWidths1);
            document.add(table6);
///////////////////
            

                   PdfPTable table12 = new PdfPTable(5);
                  // table12.setWidthPercentage(80);
            table12.setWidthPercentage(60);

            table12.getDefaultCell().setBorder(PdfPCell.NO_BORDER);

            Font fontbold5 = FontFactory.getFont("Times-Roman", 15, Font.BOLD);
            Font font5 = FontFactory.getFont("Times-Roman", 12, Font.BOLD);
            Image image5 = Image.getInstance("E:\\sripp\\sriGVP.jpg");
            PdfPTable nested13 = new PdfPTable(1);
            nested13.getDefaultCell().setBorder(PdfPCell.NO_BORDER);
           // nested3.addCell(image3);
 nested13.getDefaultCell().setHorizontalAlignment(Element.ALIGN_RIGHT);
 PdfPTable nested15 = new PdfPTable(1);
            nested15.getDefaultCell().setBorder(PdfPCell.NO_BORDER);
           // nested3.addCell(image3);
 nested15.getDefaultCell().setHorizontalAlignment(Element.ALIGN_RIGHT);
PdfPTable nested16 = new PdfPTable(1);
            nested16.getDefaultCell().setBorder(PdfPCell.NO_BORDER);
           // nested3.addCell(image3);
 nested16.getDefaultCell().setHorizontalAlignment(Element.ALIGN_RIGHT);
PdfPTable nested20 = new PdfPTable(1);
            nested20.getDefaultCell().setBorder(PdfPCell.NO_BORDER);
           // nested3.addCell(image3);
 nested20.getDefaultCell().setHorizontalAlignment(Element.ALIGN_RIGHT);
          
            
            PdfPTable nested14 = new PdfPTable(1);
            nested14.getDefaultCell().setBorder(PdfPCell.NO_BORDER);
            nested14.getDefaultCell().setHorizontalAlignment(Element.ALIGN_RIGHT);

                  nested14.addCell(image5);
           table12.addCell(nested15);   
           table12.addCell(nested20); 
table12.addCell(nested14);           
table12.addCell(nested13);              
   
   
            
   table12.addCell(nested16);
   document.add(table12);
            //////////////////////
     PdfPTable table16 = new PdfPTable(2);
            table16.setWidthPercentage(88);

            table16.getDefaultCell().setBorder(PdfPCell.NO_BORDER);

            Font fontbold11 = FontFactory.getFont("Times-Roman", 15, Font.BOLD);
            Font font11 = FontFactory.getFont("Times-Roman", 12, Font.BOLD);
           // Image image1 = Image.getInstance("E:\\sripp\\SriImage.jpg");
          // PdfPTable nested = new PdfPTable(1);
          // nested.getDefaultCell().setBorder(PdfPCell.NO_BORDER);
           // nested.addCell(image1);
 
           // table6.addCell(nested);
            PdfPTable nested11 = new PdfPTable(1);
            nested11.getDefaultCell().setBorder(PdfPCell.NO_BORDER);
            nested11.getDefaultCell().setHorizontalAlignment(Element.ALIGN_CENTER);

            nested11.addCell(new Phrase("STUDENT Recommendation Letter", fontbold11));
              Image image11 = Image.getInstance("E:\\sripp\\sriGVP.jpg");
           PdfPTable nested21 = new PdfPTable(1);
           nested21.getDefaultCell().setBorder(PdfPCell.NO_BORDER);
            nested21.addCell(new Phrase("", font11));
           table16.addCell(nested21);
         nested11.addCell(new Phrase("", font11));
           table16.addCell(nested11);
            float[] columnWidths11 = new float[]{10f, 80f};
            table16.setWidths(columnWidths11);
            document.add(table16);
   
   ///////////////////////////////////
            Chunk chunk = new Chunk();
            document.add(Chunk.NEWLINE);
            document.add(Chunk.NEWLINE);

            PdfPTable table1 = new PdfPTable(3);
            table1.getDefaultCell().setBorder(PdfPCell.NO_BORDER);

            table1.addCell(new Phrase(" ", FontFactory.getFont(FontFactory.HELVETICA, 8)));
            table1.addCell(new Phrase("", FontFactory.getFont(FontFactory.HELVETICA, 9)));
            
           java.util.Date date = new java.util.Date();  
    java.text.SimpleDateFormat formatter = new java.text.SimpleDateFormat("dd/MM/yyyy");  
    String strDate= formatter.format(date);  
            table1.addCell(new Phrase("DATE: " +strDate , FontFactory.getFont(FontFactory.HELVETICA, 8)));

            table1.addCell(new Phrase("                     ", FontFactory.getFont(FontFactory.HELVETICA, 9)));
            table1.addCell(new Phrase("                      ", FontFactory.getFont(FontFactory.HELVETICA, 9)));
           table1.addCell(new Phrase("                      ", FontFactory.getFont(FontFactory.HELVETICA, 9)));
            table1.addCell(new Phrase("                   ", FontFactory.getFont(FontFactory.HELVETICA, 9)));
            float[] columnWidths = new float[]{30f, 25f, 20f};
            table1.setWidths(columnWidths);
            document.add(table1);
            //insertCell(table2, "", Element.ALIGN_LEFT, 4, bfBold12);
 Chunk chunk1 = new Chunk();
            document.add(Chunk.NEWLINE);
            document.add(Chunk.NEWLINE);
            PdfPTable table4 = new PdfPTable(1);
            table4.getDefaultCell().setBorder(PdfPCell.NO_BORDER);
             table4.addCell(new Phrase("                             Student Name : "+ Content2, FontFactory.getFont(FontFactory.HELVETICA, 11)));
            table4.addCell(new Phrase("                            Rollno : "+ Content3, FontFactory.getFont(FontFactory.HELVETICA, 11)));
           table4.addCell(new Phrase("                             FacultyName : "+ Content4 , FontFactory.getFont(FontFactory.HELVETICA, 11)));
            table4.addCell(new Phrase("                                         Course : "+Content5, FontFactory.getFont(FontFactory.HELVETICA, 11)));
             table4.addCell(new Phrase("                                        Description : "+Content6, FontFactory.getFont(FontFactory.HELVETICA, 11)));
            table4.addCell(new Phrase("                             This certificate is issue to enable him/her to apply "+ Content7, FontFactory.getFont(FontFactory.HELVETICA, 11)));document.add(table4);
            
            
            PdfPTable table = new PdfPTable(5);
            table.getDefaultCell().setPadding(3);
          //  table.addCell(new Phrase("NAME", FontFactory.getFont(FontFactory.HELVETICA, 9)));
           // table.addCell(new Phrase("FATHER NAME ", FontFactory.getFont(FontFactory.HELVETICA, 9)));
           // table.addCell(new Phrase("COURSE", FontFactory.getFont(FontFactory.HELVETICA, 9)));
           // table.addCell(new Phrase("YEAR", FontFactory.getFont(FontFactory.HELVETICA, 9)));

            table.addCell(new Phrase("PURPOSE", FontFactory.getFont(FontFactory.HELVETICA, 9)));



           

            

           
                table.addCell(new Phrase("" + Content2, FontFactory.getFont(FontFactory.HELVETICA, 7)));

                table.addCell(new Phrase(Content3, FontFactory.getFont(FontFactory.HELVETICA, 7)));
                table.addCell(new Phrase(Content5, FontFactory.getFont(FontFactory.HELVETICA, 7)));
                table.addCell(new Phrase(Content6, FontFactory.getFont(FontFactory.HELVETICA, 7)));
                table.addCell(new Phrase("" + Content7, FontFactory.getFont(FontFactory.HELVETICA, 7)));


            
            float[] columnWidths2 = new float[]{10f, 20f, 20f, 20f, 20f};
            table.setWidths(columnWidths2);
            //document.add(table);
 Chunk chunk3 = new Chunk();
            document.add(Chunk.NEWLINE);
            document.add(Chunk.NEWLINE);
                document.add(Chunk.NEWLINE);
            document.add(Chunk.NEWLINE);    document.add(Chunk.NEWLINE);
            document.add(Chunk.NEWLINE);
            Paragraph paragraph = new Paragraph("Faculty Signature                                 ");
            paragraph.setAlignment(Element.ALIGN_RIGHT);
           document.add(paragraph);
           
           


                                 PdfPTable table10 = new PdfPTable(4);
            table10.setWidthPercentage(50);

            table10.getDefaultCell().setBorder(PdfPCell.NO_BORDER);

            Font fontbold1 = FontFactory.getFont("Times-Roman", 15, Font.BOLD);
            Font font12 = FontFactory.getFont("Times-Roman", 12, Font.BOLD);
            Image image3 = Image.getInstance("E:\\sripp\\SriImage.jpg");
            PdfPTable nested3 = new PdfPTable(1);
            nested3.getDefaultCell().setBorder(PdfPCell.NO_BORDER);
           // nested3.addCell(image3);
 nested3.getDefaultCell().setHorizontalAlignment(Element.ALIGN_RIGHT);
 PdfPTable nested5 = new PdfPTable(1);
            nested5.getDefaultCell().setBorder(PdfPCell.NO_BORDER);
           // nested3.addCell(image3);
 nested5.getDefaultCell().setHorizontalAlignment(Element.ALIGN_RIGHT);
PdfPTable nested6 = new PdfPTable(1);
            nested6.getDefaultCell().setBorder(PdfPCell.NO_BORDER);
           // nested3.addCell(image3);
 nested6.getDefaultCell().setHorizontalAlignment(Element.ALIGN_RIGHT);

           
            table10.addCell(nested3);
            table10.addCell(nested5);
            table10.addCell(nested6);
            PdfPTable nested4 = new PdfPTable(1);
            nested4.getDefaultCell().setBorder(PdfPCell.NO_BORDER);
            nested4.getDefaultCell().setHorizontalAlignment(Element.ALIGN_RIGHT);

                  nested4.addCell(image3);
   table10.addCell(nested4);
            document.add(table10);

            document.close();

            if ((new File(file)).exists()) {

                Process p = Runtime.getRuntime().exec("rundll32 url.dll,FileProtocolHandler " + file);

                p.waitFor();

            } else {

                System.out.println("File is not exists");

            }
            response.sendRedirect("stuview.jsp");


        } catch (Exception e) {
            e.printStackTrace();
        }

%>
