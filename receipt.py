# imports module 
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle 
from reportlab.lib import colors 
from reportlab.lib.pagesizes import A4 
from reportlab.lib.styles import getSampleStyleSheet 


DATA = [ 
	[ "S.No" , "Item", "Quantity", "Rate" ,"Total",], 
	[ "01", "Notebook", "5 Psc.", "100/-", "500"], 
	[ "02", "Stationary Box", "1 Psc.", "150.30/-","150.30"],
    [ "03", "Sketch Pen", "2 Pack.", "50.20/-","100.40"], 
    [ "04", "Dot Pen", "2 Psc.", "15.0/-","30.00"],  
     [ "05", "Gel Pen", "2 Psc.", "30.0/-","60.00"],  
     [ "06", "Pencil Box", "1 Box", "80.50/-","161.00"],  
	[ "Sub Total", "", "","", "1001.07/-"], 
	[ "Discount", "", "","", "1.07/-"], 
	[ "Total", "", "","", "1000.00/-"], 
] 


pdf = SimpleDocTemplate( "receipt.pdf" , pagesize = A4 ) 


styles = getSampleStyleSheet() 


title_style = styles[ "Heading1" ] 


title_style.alignment = 1

title = Paragraph( "Pament Receipt" , title_style ) 


style = TableStyle( 
	[ 
		( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.teal), 
		( "GRID" , ( 0, 0 ), ( 6, 6 ), 1 , colors.black ), 
		( "BACKGROUND" , ( 0, 0 ), ( 4, 0 ), colors.aqua), 
		( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.teal), 
		( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ), 
		( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.whitesmoke ), 
	] 
) 


table = Table( DATA , style = style ) 

pdf.build([ title , table ]) 
