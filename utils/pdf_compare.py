"""
Qxf2 Services: This script can be used to compare two pdf files
"""

from PIL import Image, ImageChops
import os,time,PythonMagick,subprocess,shutil
from optparse import OptionParser
 
class PDF_Image_Compare:    
    "Compare's two pdf files"
    def __init__(self,pdf1,pdf2):
        "Constructor: Initialises file1 and file 2"
        self.download_dir = os.getcwd()
        self.pdf1 = pdf1
        self.pdf2 = pdf2
 
 
    def get_image_list_from_pdf(self,pdf_file):
        "Return a list of images that resulted from running convert on a given pdf"
        pdf_name = pdf_file.split(os.sep)[-1].split('.pdf')[0]
        pdf_dir = pdf_file.split(pdf_name)[0]
        jpeg = pdf_file.split('.pdf')[0]+'.jpeg'
        # Convert the pdf file to jpeg file
        self.call_convert(pdf_file,jpeg)
        #Get all the jpeg files after calling convert and store it in a list
        image_list = []        
        file_list = os.listdir(pdf_dir)
        for f in file_list:
            if f[-5:]=='.jpeg' and pdf_name in f:
                #Make sure the file names of both pdf are not similar
                image_list.append(f)
 
        print('Total of %d jpegs produced after converting the pdf file: %s'%(len(image_list),pdf_file))
        return image_list
 
 
    def call_convert(self,src,dest):
        "Call convert to convert pdf to jpeg"
        try:
            subprocess.check_call(["convert",src,dest])
        except Exception,e:
            print('Convert exception ... could be an ImageMagick bug')
            print(e)
 
 
    def create_diff_image(self,pdf1_list,pdf2_list,diff_image_dir):
        "Creates the diffed images in diff image directory and generates a pdf by calling call convert"
        result_flag = True
        for pdf1_img,pdf2_img in zip(pdf1_list,pdf2_list):
            diff_filename = diff_image_dir + os.sep+'diff_' + pdf2_img
            try:
                pdf2_image = Image.open((os.path.dirname(self.pdf2))+os.sep+pdf2_img)                
                pdf1_image = Image.open((os.path.dirname(self.pdf1))+os.sep+pdf1_img)
                diff = ImageChops.difference(pdf2_image,pdf1_image)
                diff.save(diff_filename)
 
                if (ImageChops.difference(pdf2_image,pdf1_image).getbbox() is None):
                    result_flag = result_flag & True
                    print ('The pdf1 and pdf2 matched')
                else:
                    result_flag = result_flag & False
                    print ('The file didnt match for: \n>>%s\nand\n>>%s'%((os.path.dirname(self.pdf2)) +os.sep+ pdf2_img,(os.path.dirname(self.pdf1)) +os.sep+ pdf1_img))
            except Exception,e:
                print('Error when trying to open image')
                result_flag = result_flag & False
        #Create a pdf out of all the jpegs created
        diff_pdf_name = 'diff_'+pdf2_img.split('.jpeg')[0]+'.pdf'
        self.call_convert(diff_image_dir+os.sep+'*.jpeg', (os.path.dirname(self.pdf1))+os.sep+diff_pdf_name)
 
        if os.path.exists(diff_pdf_name):
            print('Successfully created the difference pdf: %s'%(diff_pdf_name))
 
        return result_flag
 
 
    def cleanup(self,diff_image_dir,pdf1_list,pdf2_list):
        "Clean up all the image files created"
        print('Cleaning up all the intermediate jpeg files created when comparing the pdf')
        for pdf1_img,pdf2_img in zip(pdf1_list,pdf2_list):
            try:
                os.remove((os.path.dirname(self.pdf1)) +os.sep+ pdf1_img)
                os.remove((os.path.dirname(self.pdf2)) +os.sep+ pdf2_img)
            except Exception,e:
                print('Unable to delete jpeg file')
                print(e)
        print('Nuking the temporary image_diff directory')
        try:
            time.sleep(5)
            shutil.rmtree(diff_image_dir)
        except Exception,e:
            print('Could not delete the image_diff directory')
            print(e)
 
 
    def get_pdf_diff(self,cleanup=True):
        "Create a difference pdf by overlaying the two pdfs and generating an image difference.Returns True if the file matches else returns false"
        result_flag = False
        #Get the list of images using get_image_list_from_pdf which inturn calls convert on a given pdf  
        pdf1_list = self.get_image_list_from_pdf(self.pdf1)
        pdf2_list = self.get_image_list_from_pdf(self.pdf2)
 
        #If diff directory already does exist - delete it 
        #Easier to simply nuke the folder and create it again than to check if its empty
        diff_image_dir = (os.path.dirname(self.pdf1)) + os.sep+'diff_images'
        if os.path.exists(diff_image_dir):
            print('diff_images directory exists ... about to nuke it')
            shutil.rmtree(diff_image_dir)
 
        #Create a new and empty diff directory
        os.mkdir(diff_image_dir)
        print('Total pages in pdf2: %d'%len(pdf2_list))
        print('Total pages in pdf1 : %d'%len(pdf1_list))
 
        #Verify that there are equal number pages in pdf1 and pdf2
        if len(pdf2_list)==len(pdf1_list) and len(pdf2_list) !=0:
            print('Check SUCCEEDED: There are an equal number of jpegs created from the pdf generated from pdf2 and pdf1')
            #print('Total pages in images: %d'%len(pdf2_list))
            pdf1_list.sort()
            pdf2_list.sort()
 
            #Create the diffed images
            result_flag = self.create_diff_image(pdf1_list,pdf2_list,diff_image_dir)
        else:
            print('Check FAILED: There are an unequal number of jpegs created from the pdf generated from pdf2 and pdf1')
            print('Total pages in image2 : %d'%len(pdf2_list))
            print('Total pages in image1: %d'%len(pdf1_list))
            print('ERROR: Skipping image comparison between %s and %s'%(self.pdf1,self.pdf2))
 
        if cleanup:
            #Delete all the image files created
            self.cleanup(diff_image_dir,pdf1_list,pdf2_list)            
 
        return result_flag


#---USAGE EXAMPLES
if __name__== '__main__':
    #Enter the path of two PDF files here
    pdf1 = 'Enter the path for the first pdf file'
    pdf2 = 'Enter the path for the second pdf file'
    
    #Intialize the pdf_obj and compare the two pdf files
    pdf_obj = PDF_Image_Compare(pdf1,pdf2)
    result_flag = test_obj.get_pdf_diff()
    if result_flag == True:
        print ('The two PDF files matched properly')
    else:
        print ('The PDFs didnt match properly, check the diff file generated')