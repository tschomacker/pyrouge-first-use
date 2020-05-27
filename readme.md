# First Use of Rouge 1.5.5 / pyrouge in Python

## Table of contents
1. [Installation](#installation)
2. [Trying the two examples](#examples)
    1. [Basic Example](#basic-example)
    2. [Excerpts from BertSum Example](#bertsum-example)
3. [Troubleshooting](#troubleshooting)

<a name="installation"></a>
## 1. Installation
| Os| Instruction |
| :- | :- |
|  Windows | https://stackoverflow.com/a/47045437/7924573 |
| Ubuntu / Linux | https://ireneli.eu/2018/01/11/working-with-rouge-1-5-5-evaluation-metric-in-python/ |

<a name="examples"></a>
## 2. Trying the two examples:

<a name="basic-example"></a>
### 2.1 Basic Example
1. ```cd basic```
1. ```python app.py```
```bash
2020-05-27 10:22:06,369 [MainThread  ] [INFO ]  Writing summaries.
2020-05-27 10:22:06,375 [MainThread  ] [INFO ]  Processing summaries. Saving system files to c:\users\thorben\appdata\local\temp\tmpkilfob\system and model files to c:\users\thorben\appdata\local\temp\tmpkilfob\model.
2020-05-27 10:22:06,375 [MainThread  ] [INFO ]  Processing files in system/.
2020-05-27 10:22:06,375 [MainThread  ] [INFO ]  Processing s_sum.1.txt.
2020-05-27 10:22:06,378 [MainThread  ] [INFO ]  Saved processed files to c:\users\thorben\appdata\local\temp\tmpkilfob\system.
2020-05-27 10:22:06,378 [MainThread  ] [INFO ]  Processing files in C:\Users\Thorben\Desktop/pyrouge/model/.
2020-05-27 10:22:06,378 [MainThread  ] [INFO ]  Processing m_sum.1.txt.
2020-05-27 10:22:06,381 [MainThread  ] [INFO ]  Saved processed files to c:\users\thorben\appdata\local\temp\tmpkilfob\model.
2020-05-27 10:22:06,382 [MainThread  ] [INFO ]  Written ROUGE configuration to c:\users\thorben\appdata\local\temp\tmpqabdy5\rouge_conf.xml
2020-05-27 10:22:06,382 [MainThread  ] [INFO ]  Running ROUGE with command perl  C:\rouge\ROUGE-1.5.5.pl -e C:\rouge\data -c 95 -2 -1 -U -r 1000 -n 4 -w 1.2 -a -m c:\users\thorben\appdata\local\temp\tmpqabdy5\rouge_conf.xml
```

```bash
---------------------------------------------
1 ROUGE-1 Average_R: 1.00000 (95%-conf.int. 1.00000 - 1.00000)
1 ROUGE-1 Average_P: 0.85714 (95%-conf.int. 0.85714 - 0.85714)
1 ROUGE-1 Average_F: 0.92308 (95%-conf.int. 0.92308 - 0.92308)
---------------------------------------------
1 ROUGE-2 Average_R: 0.80000 (95%-conf.int. 0.80000 - 0.80000)
1 ROUGE-2 Average_P: 0.66667 (95%-conf.int. 0.66667 - 0.66667)
1 ROUGE-2 Average_F: 0.72727 (95%-conf.int. 0.72727 - 0.72727)
---------------------------------------------
1 ROUGE-3 Average_R: 0.50000 (95%-conf.int. 0.50000 - 0.50000)
1 ROUGE-3 Average_P: 0.40000 (95%-conf.int. 0.40000 - 0.40000)
1 ROUGE-3 Average_F: 0.44444 (95%-conf.int. 0.44444 - 0.44444)
---------------------------------------------
1 ROUGE-4 Average_R: 0.00000 (95%-conf.int. 0.00000 - 0.00000)
1 ROUGE-4 Average_P: 0.00000 (95%-conf.int. 0.00000 - 0.00000)
1 ROUGE-4 Average_F: 0.00000 (95%-conf.int. 0.00000 - 0.00000)
---------------------------------------------
1 ROUGE-L Average_R: 1.00000 (95%-conf.int. 1.00000 - 1.00000)
1 ROUGE-L Average_P: 0.85714 (95%-conf.int. 0.85714 - 0.85714)
1 ROUGE-L Average_F: 0.92308 (95%-conf.int. 0.92308 - 0.92308)
---------------------------------------------
1 ROUGE-W-1.2 Average_R: 0.69883 (95%-conf.int. 0.69883 - 0.69883)
1 ROUGE-W-1.2 Average_P: 0.85714 (95%-conf.int. 0.85714 - 0.85714)
1 ROUGE-W-1.2 Average_F: 0.76993 (95%-conf.int. 0.76993 - 0.76993)
---------------------------------------------
1 ROUGE-S* Average_R: 1.00000 (95%-conf.int. 1.00000 - 1.00000)
1 ROUGE-S* Average_P: 0.71429 (95%-conf.int. 0.71429 - 0.71429)
1 ROUGE-S* Average_F: 0.83334 (95%-conf.int. 0.83334 - 0.83334)
---------------------------------------------
1 ROUGE-SU* Average_R: 1.00000 (95%-conf.int. 1.00000 - 1.00000)
1 ROUGE-SU* Average_P: 0.74074 (95%-conf.int. 0.74074 - 0.74074)
1 ROUGE-SU* Average_F: 0.85106 (95%-conf.int. 0.85106 - 0.85106)
```
<a name="bertsum-example"></a>
### 2.2 Excerpts from BertSum Example
1. ```cd bertsum```
1. ```python app.py```
```bash
2020-05-27 11:38:32,332 [MainThread  ] [INFO ]  Writing summaries.
2020-05-27 11:38:32,344 [MainThread  ] [INFO ]  Processing summaries. Saving system files to c:\users\thorben\appdata\local\temp\tmpcsv8xi\system and model files to c:\users\thorben\appdata\local\temp\tmpcsv8xi\model.
2020-05-27 11:38:32,345 [MainThread  ] [INFO ]  Processing files in system/.
2020-05-27 11:38:32,345 [MainThread  ] [INFO ]  Processing cnndm_step44000.candidate.
2020-05-27 11:38:32,351 [MainThread  ] [INFO ]  Saved processed files to c:\users\thorben\appdata\local\temp\tmpcsv8xi\system.
2020-05-27 11:38:32,352 [MainThread  ] [INFO ]  Processing files in model/.
2020-05-27 11:38:32,354 [MainThread  ] [INFO ]  Processing cnndm_step44000.gold.
2020-05-27 11:38:32,355 [MainThread  ] [INFO ]  Saved processed files to c:\users\thorben\appdata\local\temp\tmpcsv8xi\model.
2020-05-27 11:38:32,361 [MainThread  ] [INFO ]  Written ROUGE configuration to c:\users\thorben\appdata\local\temp\tmpkomkak\rouge_conf.xml
2020-05-27 11:38:32,361 [MainThread  ] [INFO ]  Running ROUGE with command perl  C:\rouge\ROUGE-1.5.5.pl -e C:\rouge\data -c 95 -2 -1 -U -r 1000 -n 4 -w 1.2 -a -m c:\users\thorben\appdata\local\temp\tmpkomkak\rouge_conf.xml
```

```bash
---------------------------------------------
1 ROUGE-1 Average_R: 0.75574 (95%-conf.int. 0.75574 - 0.75574)
1 ROUGE-1 Average_P: 0.42332 (95%-conf.int. 0.42332 - 0.42332)
1 ROUGE-1 Average_F: 0.54267 (95%-conf.int. 0.54267 - 0.54267)
---------------------------------------------
1 ROUGE-2 Average_R: 0.32348 (95%-conf.int. 0.32348 - 0.32348)
1 ROUGE-2 Average_P: 0.18107 (95%-conf.int. 0.18107 - 0.18107)
1 ROUGE-2 Average_F: 0.23218 (95%-conf.int. 0.23218 - 0.23218)
---------------------------------------------
1 ROUGE-3 Average_R: 0.15132 (95%-conf.int. 0.15132 - 0.15132)
1 ROUGE-3 Average_P: 0.08464 (95%-conf.int. 0.08464 - 0.08464)
1 ROUGE-3 Average_F: 0.10856 (95%-conf.int. 0.10856 - 0.10856)
---------------------------------------------
1 ROUGE-4 Average_R: 0.09226 (95%-conf.int. 0.09226 - 0.09226)
1 ROUGE-4 Average_P: 0.05157 (95%-conf.int. 0.05157 - 0.05157)
1 ROUGE-4 Average_F: 0.06616 (95%-conf.int. 0.06616 - 0.06616)
---------------------------------------------
1 ROUGE-L Average_R: 0.70492 (95%-conf.int. 0.70492 - 0.70492)
1 ROUGE-L Average_P: 0.39486 (95%-conf.int. 0.39486 - 0.39486)
1 ROUGE-L Average_F: 0.50618 (95%-conf.int. 0.50618 - 0.50618)
---------------------------------------------
1 ROUGE-W-1.2 Average_R: 0.20035 (95%-conf.int. 0.20035 - 0.20035)
1 ROUGE-W-1.2 Average_P: 0.18580 (95%-conf.int. 0.18580 - 0.18580)
1 ROUGE-W-1.2 Average_F: 0.19280 (95%-conf.int. 0.19280 - 0.19280)
---------------------------------------------
1 ROUGE-S* Average_R: 0.54338 (95%-conf.int. 0.54338 - 0.54338)
1 ROUGE-S* Average_P: 0.17037 (95%-conf.int. 0.17037 - 0.17037)
1 ROUGE-S* Average_F: 0.25941 (95%-conf.int. 0.25941 - 0.25941)
---------------------------------------------
1 ROUGE-SU* Average_R: 0.54408 (95%-conf.int. 0.54408 - 0.54408)
1 ROUGE-SU* Average_P: 0.17084 (95%-conf.int. 0.17084 - 0.17084)
1 ROUGE-SU* Average_F: 0.26003 (95%-conf.int. 0.26003 - 0.26003)
```

<a name="troubleshooting"></a>
## 3. Troubleshooting
### settings.ini
should look similiar to this:
```
[pyrouge settings]
home_dir = C:\rouge
```

### Cannot open exception db file for reading: data/WordNet-2.0.exc.db
see os-specific instruction in[Installation](#installation)
