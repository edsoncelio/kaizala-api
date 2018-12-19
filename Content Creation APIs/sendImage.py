import requests

url = 
"https://api.kaiza.la/v1/groups/df91cb37-97bf-4ccd-a8c2-b2a3ba5eac62@1/actions"

payload = "{\n  actionType: \"Image\",\n  actionBody: {\n  
\tcaption:\"Image caption\",\n    
mediaResource:\"EABRCg8C+zpD6rtp0kE4SHj1cPno4VLqhskCiWAMJnGDrCZ9vSYQmBjJ6Sf7LXmHaTrkoKgCyMs8L9Ux2NpH8+AQb/8g9rMwjdeSWP1HGDJpl7kLqT+bxqXXnSw19PWmpP5igV7o21KcFgrPhUPF7OhX8iVor4ps5IYlt+qx9zGqzJkeYJQengAj2/fwI+FJ8tGfvrLgZtwtBpM/6Ep1/X9E7cXYlGdYQcNsVZC6pao2NhlIifgRBXJ8XQFL+icoUTHLDEzXbZjt3JD4nreqgg3xmtY0EafpGxCWoKxog6nXO4qfX80U5srgAaq/t3yrBS0zZMS96k2eVV8pzM4BVhN+dLpoxCgTjwPszB/C1u/lRxMrBGkGzexKEiBHDmgibgzYldsmeIdBocTifgOOXgUaLpo1SU9X0FfnHBxGFPJ/L1kGO4Xft4FQNdFSH650q6ktqv076IYvlwCFc4k/kRtqPJkNa0kL+VoTzmIRjq1AqIfGsWb/+jGsTwlyJhnhY2hLBeT2x6pOK0e5fcnO4VZ4nLN36bIn+0SpU+GEIdPIchhhlQO1WJxjGX7idpUnFaxtUSTY1RVb7UahGjJrUVe2EDRvbV8Xbzx4apL+aFnv2P1bmwUI+zs5F5dms8+LNkykUrC/rrgMIGfD0/Jhut5DuqG5pL4lIx+OhvcREcDAGfOfsizb7+ljne4+umJZ8gNzFAexCs+q1sfuZD4NsZ8yYzAyhJs69qbMZ05JXFKVyo5vE99GVIW4e5Rydbo0dg9lzBFhLrBUOODJM2rWbVwMtitdAF5VnqKq3nGyokUDw6lSnwspNaAcXfxFqk9s3xurCKJIa7pq0GZUCrm1Eise55pvda32JAeRm3uXZ8WM09LHTPjM9mCnpZC6D/E0vcY7cwGYeaXoXEoD64cKqz+KQL5dkHrm37fQCM2XUZgLDYHc+fhSAh6IsoCSk/Yb8FP4t++ibLUwIugxFjFWFPBgZwcTH3H5gLoedCUf32aYmKe/riu+vZ3Dq1rYvWS/2wrX/2EpGU8vi6o+6K2Au2uHWzuFTtKbOxZ4SMg8oIFZOVk/gQkhf3kbDlYNTq6e6BjWYUs0yVuT+VDt1BUW0/SbzPKfoSxYt0OyJqfdSEq+WM1aoQgZC0LphLZ9Js/30qIjRt7rQgS5Yhs5g5eXlBclD22aic6nlePG904WGKooqBkXTgoxrRJsTPHbyCvwUweAX0TI0mUlXFiJ2Y8Ap2feEot6d/wa1nUSKfqjnWZpxxkL9AAxHxa8BZW3wBRNsaY+bEEth72Ju41BaYHol2sN3L8yXZvTbsSSdwG+iGzuL1dXmJ9zCDRwjTub/NiTmtAfgPilFic2tPz+LbTY/eZwd8tm066WBAItmBQVqsi3XSdGR9L2/tSuqGhGUy961USR6lUm5CzM0C2FONIllHhQMuLgyVw9VPBpz19MsHt3zKyTTtR32hCv/EmBDAWSexSLXe3THUtp13nj1iWH35IfzBF9u45wYcwVKcA26iEslSQZ8e93Vi3q0oNQlMsqt6XvUwoKVjMDEewZM9gHJbH32FzCUv7tS5CigBt3qdKn4Irw7CC/hxcfshS2Y/fOp5LF9jzs58lx/gTZycm5iB/875fplDU5QP95cf9H2wXVYiY/LROJtHCstyMSJ++t/tyuSVZSsoMCJVyqzC+9YADl9J/iOp4LZXFQA/iFdxODKjEQqmacQeUgSx/Z35pRDp2Wrxmx3DM2PHhRt0JZqJZjhKMU0sfp4QfSh/gqMCFMNz5GeWnWYUNcGRi7cZMBIFgFdbT6jOPA4cXCJG1zoX3i/fzHSLZSjgZAslIjVDjalO1VqCjb+OzJL8j64mdDKa4DdUVRdZOxrFmF2S8kIvPvhAkJmmFvqwZHRzgq11HbmBdaVt1OG3GjNGy5unHxh6gk9O8XvkdHS4OnsB6gG7y4NLYOUqdzJokZgqjFSJU5gscJrm9RRta9IIolaT4kHCZh0BviSy19LdCDQjSYKsEJeGja0QO7ivjeWImByngjubBn6TBC6cSRrExSn4i5718Bcj3RlFPbScNER761pU4b/hunHW1LQpTuFp7pXUTx+7XWb9KX0gjyhgAdVF3ZAjJAgeKNmrjk5u/CJx7v+vri1JACSi7WROcj/bA+oibOco5kpN+ldCDAx5gP3kntQQ0miKyvG+v9wRKqYj/OSSzHXErUIo8NVPw7ENBdRwoqviC8GoEblsk9GkCo7tnebccLsev4lnudehLLptTof/2JYJ5+KtyTH1K6LJ5xk6OSzwkqv6S2tRp9fbztrDvMWeZ+6mMLTyEgfjwMACNegWbjXZ+p3U5YNn7ZNT8l1gTpNzcIk0Pz3NSO3iuZKJm1eaMSLuncp1JSBukW9vZErmRO76vgF9Pfh0vnoZT7qL0ByFn8z0XFl7qSJIEmCycgp7P2abLgvjR2DAGapIskmBb9VwpuNa6J32XSaFzt6/WyBgVZcjBdYh6xHV8AncPfvl7kYuvhxOPhIJRG8jvPBzcKhBQbuZ2izl9Pyiy66Glch/zFOPzWlArG8Vt9QESaePp4PpxXRpyt3/QsuWoJLGR/xZTmKQk9F0bXY7PSG245OMhrrWT6RjmG1ULJvxUCoFouu/7nJarCB+NyD8xGhsenVTsfGfshn+Sq7h3P4XDvEnblc5kx9juUa9tGnXPBZsP32KFUhd+KfY54ZTlNwtYo/5X6G6zZelc0jIxw6WqnMfs0eZTbf35zn1eTnVERHYuLlyEBWZmFIyn1niw8rG3Du0OgUykE7Uis3aPnf2YUfmy+1Q/pWaDPJRYy1AnRRkipcEYVl5IxsTjDrM1FaK8cRAIaAsF7rhiF1lmQT5sLlJcUNQtVnkTWuPBfYTvYH78Skl6BdiMbz0vizMFwQX1U76wA6U+ZvQO9aFzGSqRUSwYipMpR8ytIVYp44yFnE182a0HWhEwrAAXGa55dZnUzlm60KfheO8lXC9t+YBssnkruQ7G+Nqvui6noJJc308WVSPnmQcw07kOBrvwo7Cfy+ggaTwxg5LpszEvZlS3HRVhYWqMenNYy+s33Ws23pMs5+LCch/rDdmD9MwXm7FB3NJTPSpnxaxsQv5cHyZZCjQjcxc0OV3nOFUXtMscui4hrDfIlA/xtjY+6G7lbDQ8Wb4iOdjoba1rmyhOPxqZeYI+NYXw/HNLxEI9qyxvZZ/GGAhtQ88HKV1NixXoShcZg6xEcbsJdKVijk+cjFmsX1kGcIrftsGwAAMOdmSbooWQjuuZcYOp1pLdPbH6A5IWXfvV6rqqlwkLa0N2GnTFcALfe1gsvnui6T3Tpa7tgblP6E5qLx3XWx+8VR+xFBY12e/8ee+FarAmA9p5bgQfc39QuoVgSgl6PxDzONvGNyz5MsBupB9dmMQdoRSL2CjsyMqIJ5NLW1bDblOCUkDchBVYlcr5f7GAyNQJtcIhTlbNxMogB/UngXlrW52GicsLccklFEPUiAyyRt8awOL+Lxs/mk7FZlq/iXjuj1lClFeSvvvc07kjVXdW01tF5VLVZtafVJ5T4n3Z8Q5GtFv8xyw0eIrqcCVoV7Q+c3Zj3HhZQhJlMjl5mVIIfcjbEsEN8jkpVUTyRZxRR+0lpIxAuJ9zlEV7WSIyNPxM1TKjBVC5e1BdnYG6I1E4xZ6iebIyE1vDMGkoMNv8irYxxgwg/GSGDvc7pCQweXZ6z7Hw5N6JNI5vzOk5eKdHcr+3NPBA8qdS1kKPg9Ap42eA3fvmFkWP/urk7LwYlNTNDvfHYBm+Laq/R/3KDlVGUft7xxExpvWiRrUGI8R50OHEnYO6deIMqc+fbocm95TvMhgNJ4g33DWdR9c4L4zY00Cq2qyJoCRDLWdmKLPfBzB2J1la8KSmErvuCw/fL4qc719V2dIuMhv0zddAKZD+7Vs4a+tFSIMGYPP8IZIEK+8J5o8vfvUaFe/IvyQ2kpxK+TizxXHs2Lcuf2WGfkZw1K3FWyiD24jStkENr2SDPtS8n5dz5NB3QSOiS0ZdGvo05BJKGVlYRZTvL3fd4DNZVre2rAb5D+csbZpmjJ0DO5yIXYBQN4P/CSu82VscEYl6eH840jArRUfb0KAd+v5hS9rdi2mJm0h/RrTLZs/4mX9O3F6SD647RCazWb8YuEUa0FT1wiXtTtmM3sDSXLT4UQWPjGv1wyXmelQ61tZUkVeQJbzI0y97Dubsmp/nikmlpqBAYfnhHqUXaiHgQmsAuh4yr4YaAcV2DV2oaeEeoOSvigdtWGrO66KshKuu/Jq0Yrt/nw1++osVZrLLGHipIDLnZKTavkIDH5A/G04P13FroPpW6P/J+UcEBpW8vkuABRPYfdxnI6Ogy2OdHiBr0cfzZYAWgXXbYm4/uhVjAi35eQJAjwVqcz6CnV5i2ciTRAAKBi6Q9XDgZr3AmRbHVL5pizG1A6bUZnkFtlRws0bU3+vC9h47iaT3Zjq9KyNcdt21meHE0UAnXgoBqpAaZR4Opt7mWlqx6CARpwpYnP6QEmiU8iyehP3Tjfv/gJOMMWF7TQS0MIpuqaciBkagKOBuiJ/h8uIAWTADqIZOkYyBctl8mPLmbTeuck37h0AiyiiSIA9+qcrfLVvuKzMviJxJkeUiXIVKvI9R1YDpAm/9EFTw79VKMeGLqixJDOdIh0cb+C2/ycHRZmSeOaNgbBwlZwEG3Q8a971a2ROHbT1eOen4veTnlHox7X/2mMbMKNDGdseb4/R5lUx2KGYBwrpw02xARMHiotyAwb8i2upXgRJGx/XXkkEuyjRBAHe7HfzVpWYTfN5LqxOqIsO6rshxb2J4z6dXIXs2ZCMG2zA3mwGRmjvEEn7mHEqSLKbHRTnU0aUzwy3cxRsAIldnsINlvTDTOiqj/36AqokVvoPDYlYoA8uQi8zSC4V1Cpc0T7KELmX8LEh4ExV/pp9yQuAq1rFkhwqiKmzUf4vpLhEx1BZFbv31pysLLyZGWwBmMi6wHpNzerGGn5CFfxkDyZ4L1Q8Uu/p29nRX2CkhgSHvFWhEkXUHESx2+YRvj2I1iPqr5FO3LJdV/ibVjmL0lL7n8U1BtrxGGrllGJuxMzVHMR7o3lkIQkdynRtYK0zzyg1PaJ9605xz0l0FdogeMbWFjBeT7osGljL9jFgN96Qtt2FFL7Gj5vKTrHGe7FNhgUl7rhzTeKJtoakGvSKDhQ+D7XYMf+n/cTdurgM5M+YzkTwcKx2c9X+MSfi5n4wFT1crvdh4krG9twYze3lJtPQq3SlF2zy/HO134x8fNxBg2BMUdu5KPmI3ZtcCLBR8X1Ga46/TyCpSlqYjLGBTMThJVIN+wFnIe2A+RXoRB9zFQN+LrzlxSFUMp8aUBIkkUEA46D8/sHWIDKKqkmOei+x399Jqd+801QQ7H2BW6/ELzyvDN11ZPBrWCe71j5wyn7cGUDYCWFhML5w/Ur4p9geFGg6QMlObmKgTogUycg0Gyq6juT/lDECnJFaPkdEPLiVS3Z4hiOG0f7s+f6yDWQbMJrZFyOyXCTazcDGJMdsqR+uhwTT8iQJZk52R+59gTYumrguI/+6lEHrHL6pftH0iqZzwswWu+5YdbWNOxlSDhy9yHGwj+Y4917fkQarK3+LFkkoHw1H25avHaMpDSw5QKwHf1yXJlmY+lo527wfW0e7v3tcTLRIPgzKWyd7TW9MsnFNnAT5HXAa4Ttms0cBsZ2+Zu0rQWu361J+rCpSj1PHVpJdgAUPa+CVKF5Ok7zdQ4s61G1wvIB5mcjRjsi28OpBm61H7DvLwgLd4gFC6zCD9AxpPH2huNVrmIUEGEE1rmPeelObGUPZZjCrxFEqm5xX//oK6ER2pLBmJ780tDN+e/df8gMiQDxxzqfcsmf+Je/ZMhofmhSJJr8m5qRHqqLg0kR2VY0FFn0Yz9U8v9n6ltHDtRlVvRn5BTy3AccEJWe//rVl+cg07D7+23HFwNbaPw6+CKyLb0Tu5r7yPAnAOfqM6Cko49YFdtG94ZTiv3kx14JfKJETHUPaCCqAA3kuGoKyRYg0f46yurfVRVRq09v3XtTZEqVmlSbaI90wpyOkX6w5mEy1Lqhwg5CT661ZZfHIKSZA3eX8IT0utr+lzyvM0/aYJAWGjyEH7/aHwYj3kwCmnf2Np3dNhFYUqJSnSprnYo6B1YvngGWJPzqsssmn37TGkQmzQg3WG7l92/OSjtf4Nnm6v6iclhhsZtHwZmr+JPrM9x9Cgy1VTTJzk7REMr6IDzjDhJhpNPLwMDkjgOy09weECMU/156LDRlqAyc+yTr6XZTU1fHUT8KJn+NpwXeHdibIH0qQ0gb0HPbKN4XsHtsIe50qhSg4d2DVtz5AsLdoXCqJ6Anr/kM3LWD0OvTR1/ctAAeYon/bxzsqAXdXD4GqkgnMu0ZtKnX9K9NRP8UmKpqui4P7AS46XSotlJ/TeraAJvpL1RJWY7rDzPeIp/FuNfBU8I3DCIfUlxVSmWAL+v18PDd7RlawpN37Jq7qvV091pc4F+mLO5xSQuMnNL5AXKS6qrepn+2iojYGiDllqKid7e++JQ0jZVKVRNPBhl8LDCFNgnEBKa7Ml4VbNQeIQQl7Y2FKN7YE8udGnYOSm7f3bp+teUG+rMNc4KTH72NELBODn2FjXITHQtC7vs+n/mJPhMPzh+5BxBNd3L/FDxM7aJTnPnas1NyyiDjpzfgv43XBERxbTsqwNVqq5TxfOw2pM0L6LWfaUfm7QfoKx7b464/xSmb0hJhymz2MtnA4Pmf8vmy/YTHpaV+nwDUfUKqKMUDoJYDSS+7RtPIb2UjsEqKn+22mVYz+9MCtjbHp8CM6EGQ9t8Wbl46UJNx9jpo1D+RpzT+7MiE3o02V/gsNH7FprIhXtTq476yFmETSvQszzG4/yrSuIb/4sBFVa0xtDaWhmAqc/Mcigyu+zwMWO8BNSW9itAsoksso+v4k0wHZ97VniESx0m4JTY6cNuadpARO/SVCRUsgD6xvmMvmAlwrG9X67XuxQqE4E+JfvhPG97qRv21CbDZZjTHrlKrPC6X7jHqpU0AHzVZNmSzcTmooztJC6AeljJtg6jVUy1Y1P+9BqiwwWMZE4jy9TdmTw1p7rk0tzthFgaPECJ/sseS8ZVevUDGGnSKfzpZiKTM4oeO5N796u4Te1L+we3K99IH6rYQR99a82QYa2ZjkK5ZrqFjUbwGCkSG0YOcY4PB1+a0nIr1Y85NCiQFjpdtN1hwZFJxQFP51d/qQRBM1OgVsxNQs+Pa09c/wM765SdrAgW9vAJktQ5OseFpmklHG3BeYbI+UmYtI13u/s5a1aDZiSrwV1dOjPBV2EXXF2pGadpAB/6F+c6R7gaaxqt4FgQtfjieySqzsK6ybqrv1Orcn6MfBbQCGxAHj8kG1QivIks2c9oro8SDKCxNd7hi0I1qMAisaD7PGOb7IJ6+W6gO47jKKxGHe00795fFycxtD3BEWnPXC15yuRRBUEwRfLPiPgroygVbht8l3JDo0lGHH/ZIdBHu3cX+gBMBznRsZ0OqgWbHBxHXSpmguDLt+TqdQ5HiSsJNv+hNntaNaJo4ae0zXbEkHigcz/vvudQUbaZj6IjsjFDoMpuqccBY9Qz0thSrh3rQ8Npw8fOI0AHQRcy6UuJLLQPaTvlMEMMT8rBAZVLT4wGA4gvswJXl1CA2uE3d7WFGn3zh39oLMD2FaeA/Z+QBfSxGG1r7WiQUQRb0RK7+uEdNUGGYgqST7Mi1hHp0yPGSUwxmhXocHmOpLWbbvu89yRDjR+VPlR7clxYhgupxzM7feyJ9W0a0jwzfRljv7QAEyG6qcgmoEZuPOJxeCbxP1UzLQkWC/sH06GRGZl+BmITk67D16NvygNSvbR2cxq6hadAtL/P4ED4xnRNStwJ+EX1CJQYZac4UlJNCzd0rPpNzTWwCj6vdgypIwsvqvXvSsJBAOIyOMMBBeoX5xtr7grWaX9cUAnuq0ce/+B+fCJDroUHxatvciVmDO0hJE/rfpcIakDc5DPTWuM/n5tbjmW8bCqxEhw/zMyQHfJHibd880/K99HD8b0gacvx0PUkXrHHSU10AUmR16qu+GVHnr0c17dErz+aU1BRagpI1GukwFj901q//Z62Wtr43UNl7uHYf5i/tsxStqWDnntchb8CPYx8DoOilQsEdZwRP9VsaSeTV92lHjL37stmuHtWcssQ5iSSxxVkdDKyzBGZq57nm/inMtYpzz1xsF2+Wvt305hYK0XFuSwgEHvlbm0r1YeW3ICzl0etAYt06PHXiizqM8iRyOWjNUgGb0HYr9oed0v1xJPEwtpTkok2idjjSU48uvVVLg4Sd7EckumjtZu04/EsU/ETAuUF5sLsFzOLfdMKz4B90pILA8T0wAjizMtflqYzJk5LLxeELprfA54gB2Ai1qPblVoNw04W8jOdP1nZk4bLjJWeibwQksrWZPO8Suz0bpNdixNs0J63DrYr5A4ci/8ieC1ebOZXRmRv7yPGOGQ6NL2/4K6cpCHlLr6qbihgq6f0SQQ0nnovd1ma3lptljZZUfl1CAfIPNQHpVheMfPkfOUFa48KNSOseiq+fWXT2iLoXGzSNfNkxf2sACjETtGDkAMQgujBVdqucuOQZsTqdBNYVSPn4JDKmDk+ldFMMrBnK1VNkS4RLUcdHWti7cFit+KSA+i1MfFC7M9a+hu07Oc2Jh7tRfMXskc++Lsw7b46bScMIaWqVXfP1gTKbssGAOX2W3GqeVQv7NIzlQTRV4aKe5ZVJqjv99WUuEOi77C4tDWfREQPm50nwnO8iw5hlQ/kBDuoJtCBZRFMFoLDp24UX5r/aIg2Rw9T67oXOqjzGcLmKg3tRWIuDn2Fvc+r9zP+vMTmwK1IXkclptTi93rYemjRYUUB+U3IdcKckzBqdL7WpXrul2jsl4fvOlrgXBkvISuLoLIlThUvlV1aQGkZ18Q7d2FkdHZYeSwJlwLFXidT1RImBo+Q72y/RWjSQCW8yQUo3u3HisJ9bT6oBhyvjku8amnavSG1IpKKB2GVuqasa7fIV5p0Fv7eDGgWSLNU/bSpLW1fbv3gLzVYhbY8N15KE5fcGqvkImx0r6aUIAdOYX+TWyhSqVPxC/VLWr9Uw0YZ5OFFLIpduZiGh65wP+Iwq9LnOa4TgPoMt5sHhobcbvO2dA==\"\n  
}\n}"
headers = {
    'Content-Type': "application/json",
    'accessToken': "",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)