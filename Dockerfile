FROM python:3.9.6
ADD TaxApp.py /
RUN pip install --upgrade pip
RUN pip install pandas
RUN pip install streamlit
CMD [ "streamlit", "run", "./TaxApp.py" ]
