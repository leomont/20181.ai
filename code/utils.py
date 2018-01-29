import os
def visualize_tree(tree, feature_names):
    from sklearn.tree import export_graphviz
    with open("/tmp/dt.dot", 'w') as f:
        export_graphviz(tree, out_file=f, impurity=False, class_names=["blue", "red"],
                        feature_names=feature_names, label="none")

    os.system("dot -Tpng /tmp/dt.dot -o /tmp/dt.png")




def plot_2Ddata_with_boundary(predict,X,y, alpha=.5):
    if predict is not None:
      n = 200
      mins,maxs = np.min(X,axis=0), np.max(X,axis=0)
      mins -= np.abs(mins)*.2
      maxs += np.abs(maxs)*.2
      d0 = np.linspace(mins[0], maxs[0],n)
      d1 = np.linspace(mins[1], maxs[1],n)
      gd0,gd1 = np.meshgrid(d0,d1)
      D = np.hstack((gd0.reshape(-1,1), gd1.reshape(-1,1)))
      p = (predict(D)*1.).reshape((n,n))
      plt.contourf(gd0,gd1,p, levels=[-0.1,0.5], alpha=0.5, cmap=plt.cm.Greys)
    plt.scatter(X[y==0][:,0], X[y==0][:,1], c="blue", alpha=alpha)
    plt.scatter(X[y==1][:,0], X[y==1][:,1], c="red", alpha=alpha)
    
hasdot = os.system("dot")
if hasdot!=0:
    print "Installing Graphviz for tree visualization"
    os.system("sudo apt-get update")
    os.system("sudo apt-get install -y graphviz")
else:
    print "Graphviz already installed"
