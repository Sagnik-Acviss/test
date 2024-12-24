# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.messages import HumanMessage,SystemMessage
# from langchain_groq import ChatGroq
# import os
# import ast
#
# def gen_searchstring_generator(brand_name, description):
#     messages = [
#         SystemMessage(content="Act as a search string generator. Generate search strings that, when used in Google, will prioritize the brand's official website as the first result."
#                               "Provide the output as a clean, comma-separated list of search string examples inside one list."
#                               "[searchstrin1,searchstrin2,....]"),
#         HumanMessage(content=f"Brand: {brand_name}\nDescription: {description}")
#     ]
#     os.environ["GROQ_API_KEY"] = "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"
#     model = ChatGroq(model="mixtral-8x7b-32768", temperature = .1)
#     result = model.invoke(messages)
#     parser = StrOutputParser()
#     raw_output = parser.invoke(result)
#     return raw_output
#
# dex = """Simple One EV Scooter — Discover Simple One's advanced features, comfort, and range. Book your own Simple One now! A combination of power, style & sustainability. Book yours and embrace next-gen..."""
# raw_output = gen_searchstring_generator(brand_name="simple energy", description=dex)
#
#
# try:
#     output_list = ast.literal_eval(raw_output)
#     print("Converted List:", output_list)
#     print("Type:", type(output_list))
# except (ValueError, SyntaxError) as e:
#     print("Error converting string to list:", e)

import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq
import os
import ast

def gen_searchstring_generator(brand_name, description):
    messages = [
        SystemMessage(content="Act as a search string generator. Generate search strings that, when used in Google, will prioritize the brand's official website as the first result."
                              "Provide the output as a clean, comma-separated list of search string examples inside one list."
                              "[searchstrin1,searchstrin2,....]"),
        HumanMessage(content=f"Brand: {brand_name}\nDescription: {description}")
    ]
    os.environ["GROQ_API_KEY"] = "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"  # Add your Groq API key here
    model = ChatGroq(model="mixtral-8x7b-32768", temperature=0.1)
    result = model.invoke(messages)
    parser = StrOutputParser()
    raw_output = parser.invoke(result)
    return raw_output

# Streamlit App
def main():
    st.title("Search String Generator")

    # Input fields
    brand_name = st.text_input("Brand Name", placeholder="Enter the brand name")
    description = st.text_area("Description", placeholder="Enter the product description")

    if st.button("Generate Search Strings"):
        if not brand_name or not description:
            st.warning("Please provide both brand name and description.")
        else:
            with st.spinner("Generating search strings..."):
                try:
                    raw_output = gen_searchstring_generator(brand_name, description)
                    try:
                        output_list = ast.literal_eval(raw_output)
                        st.success("Search strings generated successfully!")
                        st.write("### Generated Search Strings:")
                        st.write(output_list)
                    except (ValueError, SyntaxError) as e:
                        st.error(f"Error converting string to list: {e}")
                        st.write("Raw Output:", raw_output)
                except Exception as e:
                    st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
