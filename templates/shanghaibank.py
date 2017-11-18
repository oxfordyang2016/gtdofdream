import os


#represent all transctions in a hash belong a block
t1={'hash':'cf4d1e0626a5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsxavs','12wnsZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz']}
t2={'hash':'cf2d1e0626a5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvED54XCSjoFsxavs','12wnsZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz']}
t3={'hash':'cf3d1e0626a5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDf4XCSjoFsxavs','12wnsZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz']}
t4={'hash':'cffd1e0626a5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsxags','12dnsZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz']}
t5={'hash':'cfdd1e0626a5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsxfvs','12wnsZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t6={'hash':'cfgd1e0626a5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsxfvs','12wnsZdnThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t7={'hash':'cfrd1e0626a5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsxavs','12wnsZdnThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t8={'hash':'cfdd1e0626a5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsxavs','12wnsdonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t9={'hash':'cfgd1e0626a5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsxavs','12wnsfonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t10={'hash':'ch1d1e0626a5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsxavs','12wndZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t11={'hash':'cd1d1e0626a5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsxavs','12wndZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t12={'hash':'cs1d1e0626a5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsxavs','12wnfZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t13={'hash':'cf1d1e0626a5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsxavs','12wngZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t14={'hash':'cs1d1e0626a5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsxavs','12wnsZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t15={'hash':'cf1d1e0626a5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsxavs','12wnzZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t16={'hash':'cg1d1e0626a5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsxavs','12wndZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t17={'hash':'cg1d1e0626a5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsxavs','12wnsZondhYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t18={'hash':'ch1d1e0626a5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsxavs','12wnsZonshYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t19={'hash':'cg1d1e0626a5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsxavs','12wnsZonghYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t20={'hash':'cf1d1e0626d5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjosdxavs','12wnsZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t21={'hash':'cf1d1e0626s5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsdxvs','12wnsZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t22={'hash':'cf1d1e0626f5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsdavs','12wnsZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t23={'hash':'cf1d1e0626agaee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFxdsvs','12wnsZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t24={'hash':'cf1d1e0626d5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjodsxavs','12wnsZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t25={'hash':'cf1d1e062da5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XsSjoFsxavs','12wnsZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t26={'hash':'cf1d1e062sa5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XfSjoFsxavs','12wnsZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t27={'hash':'cf1d1e062ga5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCfjoFsxavs','12wnsZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t28={'hash':'cf1d1e062ha5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCsjoFsxavs','12wnsZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t29={'hash':'cf1d1e062da5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCfjoFsxavs','12wnsZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t30={'hash':'cf1d1e062da5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsxavs','12wnsZodThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t31={'hash':'cf1d1e062fa5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsxavs','12wnsZosThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t32={'hash':'cf1d1e062sa5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsxavs','12wnsZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t33={'hash':'cf1d1e062ga5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFaxavs','12wnsZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t34={'hash':'cf1d1e06dsa5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFhxavs','12wnsZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t35={'hash':'cf1d1e062da5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsxavs','12wnsZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t36={'hash':'cf1d1e062ha5aee799e38959ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsxavs','12wssZonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t37={'hash':'cf1d1e0626a5aee799e389f9ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsxavs','12wnsdonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t38={'hash':'cf1d1e0626a5aee799e389d9ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsxdvs','12wnssonThYmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t39={'hash':'cf1d1e0626a5aee799e389s9ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSjoFsxsvs','12wnsZonThsmHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}
t40={'hash':'cf1d1e0626a5aee799e389d9ee9de145646ab6d42c15551c1670a6d74ed8854f','sendpkgroup':['XhAWyjogBM4FayAcvEDr4XCSdoFsxavs','12wnsZonThamHeYTJtKch6r2mY9t2S8tGi'],'receivepk':['13CbgCnA3WJAXvimcq5hsdXJQy3tpAG8bi','13QpjKoN3ShZQq53mAt9r5RDznomibvbvz ']}

transctions=[t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22,t23,t24,t25,t26,t27,t28,t29,t30,t31,t32,t33,t34,t35,t36,t37,t38,t39,t40]


#in order to low the complexity
answerpk='XhAWyjogBM4FayAcvEDr4XCSjoFsxavs'

allcrimegroup= []

have_detected_group = [] 


#detect which transaction hash include the pk
def detecthash(answerpk):
    for  k in transctions:
		if answerpk in k['sendpkgroup']:
			allcrimegroup.append(answerpk)
    print('the transaction hash is -----')
    return transaction

#iterate all hash data to group
def checkgoupalgo():
	group=[]
	for singletransaction in transctions:
		for  pk in singletransaction['sendpkgroup']:
			if pk in detecthash('test'):
				allcrimegroup.append(pk)
        have_detected_group.append(detecthash(answerpk))
              


def testallgroup():
	for transctions in allcrimegroup:
		if transction not in have_detected_group:
			checkgoupalgo()




if __name__=='__main__':
	#testallgroup()
	print('the user have own the fellowing pk hash group')
        print([t10,t9,t3,t2]) 
    


