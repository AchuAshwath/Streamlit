from PIL import Image
import altair as alt
import pandas as pd
import streamlit as st

# image
image = Image.open("D:/achu/programs/Projects/Streamlit/dna_logo.png")
st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA

***
""")

# input section
st.header('Enter the DNA sequence')
sequence_input = ">DNA Query 2 (sample format)\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

# reading and processing input
sequence = st.text_area("sequence input ", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = "".join(sequence[1:])

st.write("""
***                        
""")

# displaying the input
st.header("INPUT (DNA Query)")
sequence

st.write("""
***                        
""")


# nucleotide counter function
def DNA_Nucleotide_counter(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('C', seq.count('C')),
        ('G', seq.count('G'))
    ])
    return d


# displaying results
st.header("DNA Nucleotide Count")
st.subheader("1. Dictionary Format")
dict_count = DNA_Nucleotide_counter(sequence)
dict_count

st.subheader("2. Text format")
st.write('There are  ' + str(dict_count['A']) + ' adenine (A)')
st.write('There are  ' + str(dict_count['T']) + ' thymine (T)')
st.write('There are  ' + str(dict_count['G']) + ' guanine (G)')
st.write('There are  ' + str(dict_count['C']) + ' cytosine (C)')

st.subheader('3. DataFrame Format')
df = pd.DataFrame.from_dict(dict_count, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotide'})
st.write(df)

st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(100)  # controls width of bar.
)
st.write(p)
