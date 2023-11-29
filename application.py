from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from sales_prediction1 import *
from tkinter import messagebox
import warnings
warnings.filterwarnings('ignore')


root = Tk()

root.title("SALES PREDICTION")
root.geometry("800x500")

bgimg= ImageTk.PhotoImage(file="C:\\Users\\Anand Kumar\\Desktop\\Sales_Prediction\\sales.jpg")
limg= Label(root, i=bgimg)
limg.grid()

def fat_update():
    return str(itemFatContententry.current())

def item_update():
    return str(itemTypeentry.current())

def outlet_update():
    return str(outletIdentry.get())

def year_update():
    return str(Yearentry.get())

def size_update():
    return str(outletSizeentry.current())

def location_update():
    return str(outletlocationTypeentry.current())

def outlet_type_update():
    return str(outletTypeentry.current())

def prediction():
    itemId = Item_Identifier_Value.get()
    itemWeight = Item_Weight_Value.get()
    itemFatContent = itemFatContententry.current()
    itemVisibility = float(Item_Visibility_Value.get())/100
    itemType = itemTypeentry.current()
    itemMRP = Item_MRP_Value.get()
    outletId = Outlet_Identifier_Value.get()
    Year = Outlet_Establishment_Year_Value.get()
    outletSize = outletSizeentry.current()
    outletlocationType = outletlocationTypeentry.current()
    outletType = outletTypeentry.current()

    print(itemId,itemWeight,itemFatContent,itemVisibility,itemType,itemMRP,outletId,Year,outletSize,outletlocationType,outletType)

    input_array=np.array([[itemId,itemWeight,itemFatContent,itemVisibility,itemType,itemMRP,outletId,Year,outletSize,outletlocationType,outletType]])
    result=RF.predict(input_array)
    messagebox.showinfo("OUTPUT",result)


Label(root,justify="center",text="SALES PREDICTION",font="Times 25 bold",padx = 400,fg="green",bg="light grey",width=40).grid(row=1,column=3)

itemId = Label(root,text="Item ID",font="calibre 15 bold")
itemWeight = Label(root,text="Item Weight",font="calibre 15 bold")
itemFatContent = Label(root,text="Item Fat Content",font="calibre 15 bold")
itemVisibility = Label(root,text="Item Visibility",font="calibre 15 bold")
itemType = Label(root,text="Item Type",font="calibre 15 bold")
itemMRP = Label(root,text="Item MRP",font="calibre 15 bold")
outletId = Label(root,text="Outlet ID",font="calibre 15 bold")
Year = Label(root,text="Outlet Est. Year",font="calibre 15 bold")
outletSize = Label(root,text="Outlet Size",font="calibre 15 bold")
outletlocationType= Label(root,text="Outlet Location Type",font="calibre 15 bold")
outletType = Label(root,text="Outlet Type",font="calibre 15 bold")


itemId.place(x = 250, y = 100)  
itemWeight.place(x = 1050, y = 100)  
itemFatContent.place(x = 250, y = 200)  
itemVisibility.place(x = 1050, y = 200)  
itemType.place(x = 250, y = 300)  
itemMRP.place(x = 1050, y = 300)  
outletId.place(x = 250, y = 400)
Year.place(x = 1050, y = 400)  
outletSize.place(x = 250, y = 500)  
outletlocationType.place(x = 1050, y = 500)  
outletType.place(x = 250, y = 600)



Item_Identifier_Value = StringVar()
Item_Identifier_Value.set( "Enter Id" ) 

Item_Weight_Value = StringVar()
Item_Weight_Value.set( "Enter Weight" ) 

Item_Fat_Content_Value = StringVar()
Item_Fat_Content_Value.set( "Select Fat" ) 

Item_Visibility_Value = StringVar()
Item_Visibility_Value.set( "Enter visibility percentage" )

Item_Type_Value = StringVar()
Item_Type_Value.set( "Select Item Type" ) 

Item_MRP_Value = StringVar()
Item_MRP_Value.set( "Enter MRP" ) 

Outlet_Identifier_Value = StringVar()
Outlet_Identifier_Value.set( "Outlet ID" ) 

Outlet_Establishment_Year_Value = StringVar()
Outlet_Establishment_Year_Value.set( "Select Year" ) 

Outlet_Size_Value = StringVar()
Outlet_Size_Value.set( "Select Outlet Size" ) 

Outlet_Location_Type_Value = StringVar()
Outlet_Location_Type_Value.set( "Select Location" ) 

Outlet_Type_Value = StringVar()
Outlet_Type_Value.set( "Select outlet Type" ) 


itemIdentry = Entry(root,textvariable=Item_Identifier_Value)
itemIdentry.place(x = 550,y=100,height=30,width=300)

itemWeightentry = Entry(root,textvariable=Item_Weight_Value)
itemWeightentry.place(x = 1350,y=100,height=30,width=300)

itemFatContententry = ttk.Combobox(root,values = ('Low Fat','Regular'),textvariable=Item_Fat_Content_Value,font="calibre 10 normal")
itemFatContententry.place(x = 550,y=200,height=30,width=300)
Item_Fat_Content_Value.trace('w',fat_update)

itemVisibilityentry = Entry(root,textvariable=Item_Visibility_Value)
itemVisibilityentry.place(x = 1350,y=200,height=30,width=300)

items = ('Baking Goods','Breads','Breakfast','Canned','Dairy','Frozen Food','Fruits and Vegetables','Hard Drink','Health and Hygiene','Households','Meat','Others','Seafood','Snacks','Soft drinks','Starchy Food')
itemTypeentry = ttk.Combobox(root,values = items,textvariable=Item_Type_Value,font="calibre 10 normal")
itemTypeentry.place(x = 550,y=300,height=30,width=300)
Item_Type_Value.trace('w',item_update)

itemMRPentry = Entry(root,textvariable=Item_MRP_Value)
itemMRPentry.place(x = 1350,y=300,height=30,width=300)

outletIdentry = ttk.Combobox(root,values = (1,2,3,4,5,6,7,8,9),textvariable=Outlet_Identifier_Value,font="calibre 10 normal")
outletIdentry.place(x = 550,y=400,height=30,width=300)
Outlet_Identifier_Value.trace('w',outlet_update)

year = tuple(list(x for x in range(1984,2024)))
Yearentry = ttk.Combobox(root,values=year,textvariable=Outlet_Establishment_Year_Value,font="calibre 10 normal")# Yearentry.insert(0,"IN pascal")
Yearentry.place(x = 1350,y=400,height=30,width=300)
Outlet_Identifier_Value.trace('w',year_update)

outletSizeentry = ttk.Combobox(root,values = ('High','Medium','Small'),textvariable=Outlet_Size_Value,font="calibre 10 normal")# outletSizeentry.insert(0,"IN oktas")
outletSizeentry.place(x = 550,y=500,height=30,width=300)
Outlet_Identifier_Value.trace('w',size_update)

outletlocationTypeentry = ttk.Combobox(root,values = ('Tier 1','Tier 2','Tier 3'),textvariable=Outlet_Location_Type_Value,font="calibre 10 normal")# outletlocationTypeentry.insert(0,"IN oktas")
outletlocationTypeentry.place(x = 1350,y=500,height=30,width=300)
Outlet_Location_Type_Value.trace('w',location_update)

outletTypeentry = ttk.Combobox(root,values = ('Grocery Store','Supermarket Type1','Supermarket Type2','Supermarket Type3'),textvariable=Outlet_Type_Value,font="calibre 10 normal")# outletTypeentry.insert(0,"IN celsius")
outletTypeentry.place(x = 550,y=600,height=30,width=300)
Outlet_Type_Value.trace('w',outlet_type_update)

button = Button(root,text="Submit",width=12,font="Times 15 bold",command=prediction).place(x=700,y=850)

root.mainloop()