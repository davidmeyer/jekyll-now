#
#	k-prototypes.py
#
#       Run k-prototypes on (netflow) data, which inspiration (pandas) from Ed Henry
#
#	code: https://github.com/nicodv/kmodes
#
#	See "A New Approach to Data Driven Clustering", Azran, A., et al. 
#	http://mlg.eng.cam.ac.uk/zoubin/papers/AzrGhaICML06.pdf
#
#	See also
#
#	"Extensions to the k-Means Algorithm for Clustering Large Data Sets
#	with Categorical Values", Zhexue Huang
#	http://www.cse.ust.hk/~qyang/537/Papers/huang98extensions.pdf
#
#
#	David Meyer
#	dmm@1-4-5.net
#	Fri Jan 22 12:02:45 2016
#
#	$Header: $
#
#
#
#       imports
#
import sys
import time
import numpy as np
import pandas as pd
from   kmodes import kmodes
from   kmodes import kprototypes
#
#
#       globals
#
DEBUG         = 2                               # set to 1 to debug, 2 for more
verbose       = 0                               # kmodes debugging
nrows         = 30                              # number of rows to read (resources)
#
#       These are the "categorical" fields in CSV
#
categorical_field_names = ['protocol', 'src_tos', 'tcp_flags','ipv4_src_addr',
                           'l4_src_port', 'ipv4_dst_addr', 'l4_dst_port',
                           'input_snmp', 'output_snmp', 'direction', 'icmp_type']
#
#       build DataFrame
#
df = pd.DataFrame()
#
#       CSV here
#
CSV_IN  = "./data/secondout.csv"                    # data file
CSV_OUT = "./data/kprototypes.csv"
#
#       read CSV into a pandas dataframe
#
#       NB: control the number of records read (nrows) here (save some resources perhaps)
#
df = pd.read_csv(CSV_IN, sep=',', nrows=nrows,header=0)
#
#       strip whitespace (should get this done at export time)
#
df.rename(columns=lambda x: x.strip(), inplace = True)
#
#       Drop NA and NaN values
#
df = df.dropna()
#
#       Ensure things are dtype="category" (cast)
#
for c in categorical_field_names:
    df[c] = df[c].astype('category')
#
#       get a list of the catgorical indicies
#
categoricals_indicies = []
for col in categorical_field_names:
        categoricals_indicies.append(categorical_field_names.index(col))
#
#       add non-categorical fields
#
fields = list(categorical_field_names)
fields.append('in_pkts')
fields.append('in_bytes')
#
#       select fields
#
data_cats = df.loc[:,fields]
#
#       normalize continous fields
#
#       essentially compute the z-score
#
#       note: Could use (x.max() - x.min()) instead of np.std(x)
#
columns_to_normalize     = ['in_pkts', 'in_bytes']
df[columns_to_normalize] = df[columns_to_normalize].apply(lambda x: (x - x.mean()) / np.std(x))
#
#       kprototypes needs an array
#
data_cats_matrix = data_cats.as_matrix()
#
#       model parameters
#
init       = 'Huang'                    # init can be 'Cao', 'Huang' or 'random'
n_clusters = 4                          # how many clusters (hyper parameter)
max_iter   = 100                        # default 100
#
#       get the model
#
kproto = kprototypes.KPrototypes(n_clusters=n_clusters,init=init,verbose=verbose)
#
#       fit/predict
#
clusters = kproto.fit_predict(data_cats_matrix,categorical=categoricals_indicies)
#
#       combine dataframe entries with resultant cluster_id
#
proto_cluster_assignments = zip(data_cats_matrix,clusters)
#
#
if (DEBUG > 2):
        print '\nclusters:{}\nproto_cluster_assignments: {}\n'.format(clusters,proto_cluster_assignments)
#
#       Instantiate dataframe to house new cluster data
#
cluster_df = pd.DataFrame(columns=('protocol','ipv4_src_addr', 'l4_src_port',
                                   'ipv4_dst_addr','l4_dst_port','in_pkts',
                                   'in_bytes','cluster_id'))
#
#       load arrays back into a dataframe
#
for array in proto_cluster_assignments:
        cluster_df = cluster_df.append({'protocol':array[0][0],'ipv4_src_addr':array[0][1], 'l4_src_port':array[0][2],
                                    'ipv4_dst_addr':array[0][3],'l4_dst_port':array[0][4],'in_pkts':array[0][5],
                                    'in_bytes':array[0][6],'cluster_id':array[1]}, ignore_index=True)


#
#       quickly print out what we got
#
#       needs viz
#
#       c2n - cluster2name
#
c2n = []
#
#       build the list
#
for i in range(n_clusters):
	c2n.append([])
#
#       collect the elements
#
for x in proto_cluster_assignments:
        c2n[x[1]].append(x[0])

for index, record in enumerate(c2n):
    print 'cluster: {} ({})'.format(index,len(record))
    for i in record:
        print '\t{}_{}_{}_{}_({},{})'.format(i[3],i[4],i[5],i[6],i[11],i[12])
    

#
#       Save results as CSV
#
cluster_df.to_csv(CSV_OUT,index=False)

