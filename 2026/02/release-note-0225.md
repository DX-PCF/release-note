
# Title: February 24, 2026 
Link: https://docs.cloud.google.com/release-notes#February_24_2026<br>
はい、承知いたしました。Google Cloud のインフラエンジニアとして、ご提示いただいたリリースノートについて、構築済みのサービスへの影響調査を行い、簡潔に回答いたします。

---

# Google Kubernetes Engine

## Change

原文:
Expanded coverage for compute flexible committed use discounts (CUDs) is available to all Cloud Billing accounts. All Cloud Billing accounts have been automatically migrated to the new spend-based CUD model and you no longer need to opt in to benefit from the expanded coverage. For the full list of eligible SKUs across Compute Engine, GKE, and Cloud Run, see SKU Groups - Compute Flexible CUD Eligible SKUs.
To learn more about compute flexible CUDs and how they apply to your GKE usage, see the GKE CUDs documentation.

説明：
Compute Engine、GKE、Cloud Run にわたるコンピューティングリソース向けのフレキシブルなコミットメント利用割引（CUDs）の適用範囲が、すべての Cloud Billing アカウントで利用可能になりました。これにより、従来の CUD を利用していた、または利用を検討していたお客様は、より広範なリソースに対して割引が適用される可能性があります。
すべての Cloud Billing アカウントは、新しい「消費額ベース（spend-based）」の CUD モデルに自動的に移行されており、この拡大された適用範囲の恩恵を受けるためのオプトインは不要になりました。対象となる SKU の完全なリストは、提供されているドキュメントで確認できます。GKE の利用が CUD にどのように適用されるかについては、GKE CUDs のドキュメントを参照してください。

影響有無：**影響なし（むしろ正の恩恵あり）**
この変更は、GKE を含む対象サービスのコスト最適化に関するものです。既存の GKE ワークロードの機能や動作に直接的な変更や非互換性はありません。むしろ、CUD を利用している場合、または将来利用する可能性がある場合に、より柔軟で広範な割引が自動的に適用される可能性があり、コスト削減に繋がる「正の恩恵」があります。ユーザー側での設定変更や操作は不要です。

対処方法：**なし（監視推奨）**
自動的に新しいモデルに移行されるため、お客様側で特別な対処は不要です。
ただし、コスト削減の恩恵を最大限に受けているかを確認するため、Cloud Billing レポートを定期的に確認し、新しい CUD モデルがどのように適用されているかを監視することをお勧めします。必要に応じて、提供されているドキュメント（[GKE CUDs documentation](https://docs.cloud.google.com/kubernetes-engine/cud) や [SKU Groups - Compute Flexible CUD Eligible SKUs](https://cloud.google.com/skus/sku-groups/compute-flexible-cud-eligible-skus)）を確認し、請求状況を理解してください。

用語説明：
*   **コミットメント利用割引（Committed Use Discounts, CUDs）**: Google Cloud のリソースを一定期間（通常1年または3年）利用することを約束することで得られる大幅な割引です。
*   **Compute Flexible CUDs**: Compute Engine、Google Kubernetes Engine (GKE)、Cloud Run など、特定のコンピューティングリソースの利用に対して柔軟に適用される CUD です。特定の仮想マシンタイプやリージョンに縛られず、対象となるコンピューティングリソースの利用総額に対して割引が適用されます。
*   **Spend-based CUD model（消費額ベース CUD モデル）**: 従来の SKU ベースではなく、対象となるリソースの総消費額（ドル建て）に基づいて割引が適用される CUD モデルです。これにより、異なる SKU やリージョンを横断して利用したリソースに対しても割引が適用されやすくなります。
*   **SKU (Stock Keeping Unit)**: Google Cloud の各サービスにおける課金の最小単位を指します。例えば、特定の種類のVMインスタンスやストレージの量などがSKUとして定義されます。