import fitz
import pandas as pd
import os

def get_path():
    paths= []
    path1 = input('Enter the path for AI file')
    paths.append(path1)
    path2 = input('Enter the path for web files')
    paths.append(path2)
    print(paths)
    return paths

def get_final_dataframe(path, flag):
    df = pd.DataFrame(columns=['Text','label'])
    content = []
    for file in os.listdir(path):
        if file.endswith('.pdf'):
            print('--------------------------------------------------pdf-------------------------------------------`')
            doc = fitz.open(path+'\\'+file)
            print(f'doc file is : {doc}')
            content_temp=''
            for page in range(len(doc)):
                content_temp = content_temp + doc[page].get_text()
            content.append(content_temp)
    df['Text'] = content
    df['label']=flag
    print(df)
    return df

def get_content_of_pdfs(file_path):
    for path in file_path:
        if '\\AI' in path:
            df_ai = get_final_dataframe(path,1)
            print('ai files path')
        elif '\\WEB'in path:
            df_web = get_final_dataframe(path,0)
            print('web file path')
    df = df_ai.append(df_web) 
    return df


def get_content(file_path):
    # df = pd.DataFrame(columns=['Text','label'])
    df = get_content_of_pdfs(file_path)

def dataset_generate():
    print('hello')
    file_path = get_path()
    dataset = get_content(file_path)
    print(dataset)
    dataset.to_csv('dataset.csv')

if __name__ == '__main__':
    print("maiin module")
    dataset_generate()

# print(f'module= {__name__}')
# dataset_generate()
