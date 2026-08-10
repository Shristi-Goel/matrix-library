class Matrix:
    def __init__(self,rows,cols):
        self.rows=rows
        self.cols=cols
        self.data=[]
        for i in range(rows):
            row=[]
            for j in range(cols):
                row.append(0)
                
            self.data.append(row)

    def input_data(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j]=int(input(f"Enter the [{i}][{j}] element : "))

    def display(self):
        print("Displaying the matrix :")

        for row in self.data:
            for element in row:
                print(element,end=" ")
            print()

    def menu(self,other):
        user_input=input("""Hello !!!

            1. Enter 1 if you want to do addition
            2. Enter 2 if you want to do subtraction
            3. Enter 3 if you want to do a transpose
            4. Enter 4 if you want to do a multiplication
            5. Enter 5 if you want to find a determinant
            6. Enter 6 to exit

            """)
        if user_input=='1':
            self.addition(other)

        elif user_input=='2':
            self.subtraction(other)

        elif user_input=='3':
            self.transpose()

            
        elif user_input=='4':
            self.multiplication(other)

        elif user_input=='5':
            self.determinant()
            
        else:
            print("Bye....")
            
    def addition(self,other):
        if self.rows==other.rows and self.cols==other.cols:
            result=Matrix(self.rows,self.cols)
            for i in range(self.rows):
                
                for j in range(self.cols):
                    result.data[i][j]=self.data[i][j]+other.data[i][j]

            print("Addition: ")
            result.display()
            print()
            return result
        else: print("Addition is only possible in same number of rows and columns")
        

    def subtraction(self,other):
        if self.rows==other.rows and self.cols==other.cols:
            result=Matrix(self.rows,self.cols)
            for i in range(self.rows):
                
                for j in range(self.cols):
                    result.data[i][j]=self.data[i][j]-other.data[i][j]
            print("Subtraction: ")
            print()
            result.display()
            return result
        else: print("Subtraction is possible only in same number of rows and columns")
        

    def transpose(self):
        result=Matrix(self.cols,self.rows)
        print("The transpose of the matrix is :")
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[j][i]=self.data[i][j]
        
        result.display()
        print()
        return result
        
    


    def multiplication(self,other):
        if self.cols==other.rows:
            result=Matrix(self.rows,other.cols)
            second_matrix=other.transpose()
            
            for i in range(self.rows):
                
                for j in range(second_matrix.rows):
                    result_element=0
                    for element, other_element in zip(self.data[i],second_matrix.data[j]):
                        result_element+=element*other_element
                    result.data[i][j]=result_element
            print("Multiplication: ")
            result.display()
            print() 
            return result
        
        else: print("These matrices can't be multiplied together!!! ")
    def minor(self,m,n):
        result=[]
        for i in self.rows:
            arr=[]
            for j in self.cols:
                
                if i==m:
                    continue
                    if j==n:
                        continue
                        
                        element=self.data[i][j]
                        arr.append(element)
            result.append(arr)
        det=result[0][0]*result[1][1]-result[0][1]*result[1][0]
        return det
        
    def determinant(self):
        if self.rows==self.cols:
            if self.rows==1:
                result=self.data
                
            elif self.rows==2:
                result=self.data[1][1]*self.data[0][0]-self.data[0][1]*self.data[1][0]   
            
            elif self.rows>2:
                result=0
                for j in range(self.cols):
                    element=self.data[0][j]*(self.minor(0,j))*(-1)**j
                    result+=element
        print("Determinant: ",result)
                return result
                    
            
        else:
            print("Determinant is only be find out of square matrix")  

  



