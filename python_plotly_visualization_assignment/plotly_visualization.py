import pandas as pd
import plotly.express as px
epochs = range(1, 11)
loss = [0.95, 0.88, 0.80, 0.72, 0.65, 0.58, 0.50, 0.44, 0.41, 0.40]
df = pd.DataFrame({'Epoch': epochs, 'Loss': loss})
fig = px.line(df, 
              x='Epoch',
              y='Loss', 
              title='Training Loss Over Epochs', 
              markers=True)
fig.update_layout(xaxis_title='Epoch', 
                  yaxis_title='Loss')
fig.add_annotation(x=9, 
                   y=0.41, 
                   text="Loss stabilizes here", 
                   showarrow=True, 
                   arrowhead=1)

fig.show()