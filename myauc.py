
def scoreClickAUC(num_clicks, num_impressions, predicted_ctr):  
    """ 
    Calculates the area under the ROC curve (AUC) for click rates 

    Parameters 
    ---------- 
    num_clicks : a list containing the number of clicks 

    num_impressions : a list containing the number of impressions 

    predicted_ctr : a list containing the predicted click-through rates 

    Returns 
    ------- 
    auc : the area under the ROC curve (AUC) for click rates 
    """  
    i_sorted = sorted(range(len(predicted_ctr)),key=lambda i: predicted_ctr[i],  
            reverse=True)  
    auc_temp = 0.0  
    click_sum = 0.0  
    old_click_sum = 0.0  
    no_click = 0.0  
    no_click_sum = 0.0  
    
    # treat all instances with the same predicted_ctr as coming from the  
    # same bucket  
    last_ctr = predicted_ctr[i_sorted[0]] + 1.0  
    
    for i in range(len(predicted_ctr)):  
        if last_ctr != predicted_ctr[i_sorted[i]]:  
            auc_temp += (click_sum+old_click_sum) * no_click / 2.0  
            old_click_sum = click_sum  
            no_click = 0.0  
            last_ctr = predicted_ctr[i_sorted[i]]  
        no_click += num_impressions[i_sorted[i]] - num_clicks[i_sorted[i]]  
        no_click_sum += num_impressions[i_sorted[i]] - num_clicks[i_sorted[i]]  
        click_sum += num_clicks[i_sorted[i]]  
        print('auc_temp=%.2f' % auc_temp)
        print('click_sum=%.2f' % click_sum)
        print('no_click_sum=%.2f' % no_click_sum)
        print('-------------------------------------\n')
    auc_temp += (click_sum+old_click_sum) * no_click / 2.0  
    print('auc_temp=%.2f' % auc_temp)
    print('click_sum=%.2f' % click_sum)
    print('no_click_sum=%.2f' % no_click_sum)
    print('-------------------------------------\n')
    auc = auc_temp / (click_sum * no_click_sum)  
    return auc


def load_data(fin_file):
    show = []
    click = []
    score = []
    for line in open(fin_file):
        tup = line.rstrip().split('\t')
        if tup[0] != '1':
            continue
        show.append(float(tup[5]))
        click.append(float(tup[6]))
        score.append(float(tup[9]))
    return (show, click, score)

(show, click, ctr) = load_data('auc_info_20140428_mobilephone.txt')
auc = scoreClickAUC(click, show, ctr)

#print(click)
#print(show)
#print(ctr)
print(auc)
