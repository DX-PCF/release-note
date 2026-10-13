
# Title: October 12, 2026 
Link: https://docs.cloud.google.com/release-notes#October_12_2026<br>
Google Cloudインフラエンジニアとして、ご提供いただいたリリースノートに基づき、Cloud Service Meshに関する影響調査結果を報告いたします。

---

# Cloud Service Mesh (バージョン 1.30.5-asm.8)

## Announcement
原文: **1.30.5-asm.8 is now available for in-cluster Cloud Service Mesh.**
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.30.5-asm.8 uses Envoy v1.38.7-dev.
This release resolves the security vulnerability listed in Security Bulletin GCP-2026-067.
説明：
Cloud Service Mesh のバージョン 1.30.5-asm.8 が、クラスタ内デプロイ（in-cluster）向けにリリースされました。このバージョンは Envoy v1.38.7-dev を使用しており、セキュリティ速報 GCP-2026-067 で特定されたセキュリティ脆弱性を解決しています。アップグレードに関する詳細は、提供されているドキュメントリンクを参照してください。
影響有無：
**影響なし（ポジティブな影響あり）**
このアナウンス自体が既存の機能に直接的な変更を加えるものではありません。しかし、このリリースにはセキュリティ脆弱性（GCP-2026-067）の修正が含まれているため、Cloud Service Mesh を利用している環境においては、セキュリティ体制の強化に繋がるポジティブな影響があります。現在、ご提示の環境であるGoogle Cloud Composer2はCloud Service Meshを直接利用していません。ただし、Composerが稼働するGKEクラスタにCloud Service Meshを独自に導入している場合は、関連します。
対処方法：
現在 Cloud Service Mesh を利用している場合は、セキュリティリスクを軽減するため、本バージョンへのアップグレードを強く推奨します。アップグレード手順については、[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) を参照してください。

## Fixed
原文: Patch 1.30.5-asm.8 contains the fix for the following platform CVEs:
| CVE | Proxy | Control Plane | Distroless | CNI | Severity |
| --- | --- | --- | --- | --- | --- |
| CVE-2026-18924 | Yes | Yes | No | Yes | Medium (9.1) |
| CVE-2026-82474 | Yes | Yes | No | Yes | Medium (8.5) |
| CVE-2026-82209 | Yes | Yes | No | Yes | Medium (8.2) |
| CVE-2026-84782 | Yes | Yes | No | Yes | High (8.2) |
| CVE-2026-96512 | Yes | Yes | No | Yes | Medium (7.8) |
| CVE-2026-80230 | Yes | Yes | No | Yes | Medium (7.5) |
| CVE-2026-13608 | Yes | Yes | No | Yes | Medium (7.4) |
| CVE-2026-15534 | Yes | Yes | No | Yes | Medium (5.7) |
| CVE-2026-19487 | Yes | Yes | No | Yes | Medium (5.3) |
| CVE-2026-35189 | Yes | Yes | No | Yes | Low (5.3) |
| CVE-2026-75805 | Yes | Yes | No | Yes | Low (5.3) |
| CVE-2026-75806 | Yes | Yes | No | Yes | Low (5.3) |
| CVE-2026-54872 | Yes | Yes | No | Yes | Low (3.7) |
| CVE-2026-77696 | Yes | Yes | No | Yes | Low (3.7) |
| CVE-2026-0799 | Yes | Yes | No | Yes | Medium (0.0) |
説明：
このパッチリリース (1.30.5-asm.8) には、Cloud Service Mesh の以下のコンポーネント（プロキシ、コントロールプレーン、CNI）に関連する多数のプラットフォームCVE（共通脆弱性識別子）に対する修正が含まれています。修正されたCVEの深刻度（Severity）は中（Medium）から低（Low）まで幅広く、CVSSスコアが8.2の「High」な脆弱性 (CVE-2026-84782) も含まれています。
影響有無：
**影響なし（ポジティブな影響あり）**
このリリースは、既存のセキュリティ脆弱性を修正するものであり、機能的な変更や非互換性のある変更は含まれていません。したがって、既存のワークロードや設定への直接的な影響はありません。むしろ、これらの多数の脆弱性、特に深刻度「High」の脆弱性 (CVE-2026-84782) が修正されることにより、Cloud Service Mesh 環境全体のセキュリティが大幅に向上します。
対処方法：
Cloud Service Mesh を利用している場合、これらのセキュリティ修正は非常に重要であるため、速やかに本バージョンへのアップグレードを検討することを強く推奨します。アップグレードの際は、公式ドキュメントの手順に従い、テスト環境での動作確認を行ってください。

---

# Cloud Service Mesh (バージョン 1.29.8-asm.8)

## Announcement
原文: **1.29.8-asm.8 is now available for in-cluster Cloud Service Mesh.**
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.29.8-asm.8 uses Envoy v1.37.9-dev.
This release resolves the security vulnerability listed in Security Bulletin GCP-2026-067.
説明：
Cloud Service Mesh のバージョン 1.29.8-asm.8 が、クラスタ内デプロイ（in-cluster）向けにリリースされました。このバージョンは Envoy v1.37.9-dev を使用しており、セキュリティ速報 GCP-2026-067 で特定されたセキュリティ脆弱性を解決しています。アップグレードに関する詳細は、提供されているドキュメントリンクを参照してください。
影響有無：
**影響なし（ポジティブな影響あり）**
上記 1.30.5-asm.8 と同様に、このアナウンス自体が既存の機能に直接的な変更を加えるものではありません。セキュリティ脆弱性（GCP-2026-067）の修正が含まれるため、Cloud Service Mesh を利用している環境においては、セキュリティ体制の強化に繋がるポジティブな影響があります。
対処方法：
現在 Cloud Service Mesh を利用している場合、特に 1.29 系列のバージョンを使用している場合は、セキュリティリスクを軽減するため、本バージョンへのアップグレードを強く推奨します。アップグレード手順については、[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/upgrade/upgrade) を参照してください。

## Fixed
原文: Patch 1.29.8-asm.8 contains the fix for the following platform CVEs:
(CVEリストは1.30.5-asm.8と同じため省略)
説明：
このパッチリリース (1.29.8-asm.8) には、上記 1.30.5-asm.8 と同様に、Cloud Service Mesh のプロキシ、コントロールプレーン、CNIコンポーネントに関連する多数のプラットフォームCVEに対する修正が含まれています。深刻度「High」の脆弱性 (CVE-2026-84782) を含む複数のCVEが修正されています。
影響有無：
**影響なし（ポジティブな影響あり）**
上記 1.30.5-asm.8 と同様に、このリリースは既存のセキュリティ脆弱性を修正するものであり、機能的な変更や非互換性のある変更は含まれていません。したがって、既存のワークロードや設定への直接的な影響はありません。これらの脆弱性が修正されることにより、Cloud Service Mesh 環境全体のセキュリティが向上します。
対処方法：
Cloud Service Mesh を利用している場合、これらのセキュリティ修正は非常に重要であるため、速やかに本バージョンへのアップグレードを検討することを強く推奨します。アップグレードの際は、公式ドキュメントの手順に従い、テスト環境での動作確認を行ってください。

---

# Cloud Service Mesh (バージョン 1.28.10-asm.49)

## Announcement
原文: **1.28.10-asm.49 is now available for in-cluster Cloud Service Mesh.**
For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.28.10-asm.49 uses Envoy v1.36.10-dev.
説明：
Cloud Service Mesh のバージョン 1.28.10-asm.49 が、クラスタ内デプロイ（in-cluster）向けにリリースされました。このバージョンは Envoy v1.36.10-dev を使用しています。アップグレードに関する詳細は、提供されているドキュメントリンクを参照してください。
影響有無：
**影響なし（ポジティブな影響あり）**
このアナウンス自体が既存の機能に直接的な変更を加えるものではありません。このリリースは主にセキュリティ修正を目的としているため、Cloud Service Mesh を利用している環境においては、セキュリティ体制の強化に繋がるポジティブな影響があります。このバージョンに関するアナウンスには、GCP-2026-067に関する明示的な記載はありませんが、Fixedセクションで多数のCVEが修正されていることが示されています。
対処方法：
現在 Cloud Service Mesh を利用している場合、特に 1.28 系列のバージョンを使用している場合は、セキュリティリスクを軽減するため、本バージョンへのアップグレードを強く推奨します。アップグレード手順については、[Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade) を参照してください。

## Fixed
原文: Patch 1.28.10-asm.49 contains the fix for the following platform CVEs:
(CVEリストは1.30.5-asm.8, 1.29.8-asm.8とほぼ同じだが、CVE-2026-81870が追加されているため注意)
| CVE | Proxy | Control Plane | Distroless | CNI | Severity |
| --- | --- | --- | --- | --- | --- |
| CVE-2026-18924 | Yes | Yes | No | Yes | Medium (9.1) |
| CVE-2026-82474 | Yes | Yes | No | Yes | Medium (8.5) |
| CVE-2026-82209 | Yes | Yes | No | Yes | Medium (8.2) |
| CVE-2026-84782 | Yes | Yes | No | Yes | High (8.2) |
| CVE-2026-96512 | Yes | Yes | No | Yes | Medium (7.8) |
| CVE-2026-80230 | Yes | Yes | No | Yes | Medium (7.5) |
| CVE-2026-13608 | Yes | Yes | No | Yes | Medium (7.4) |
| CVE-2026-15534 | Yes | Yes | No | Yes | Medium (5.7) |
| CVE-2026-19487 | Yes | Yes | No | Yes | Medium (5.3) |
| CVE-2026-35189 | Yes | Yes | No | Yes | Low (5.3) |
| CVE-2026-75805 | Yes | Yes | No | Yes | Low (5.3) |
| CVE-2026-75806 | Yes | Yes | No | Yes | Low (5.3) |
| CVE-2026-54872 | Yes | Yes | No | Yes | Low (3.7) |
| CVE-2026-77696 | Yes | Yes | No | Yes | Low (3.7) |
| CVE-2026-81870 | Yes | Yes | Yes | Yes | Low (2.0) |
| CVE-2026-0799 | Yes | Yes | No | Yes | Medium (0.0) |
説明：
このパッチリリース (1.28.10-asm.49) には、Cloud Service Mesh のプロキシ、コントロールプレーン、CNIコンポーネントに関連する多数のプラットフォームCVEに対する修正が含まれています。深刻度「High」の脆弱性 (CVE-2026-84782) を含む複数のCVEが修正されており、特にこのバージョンではCVE-2026-81870 (Low) の修正も含まれます。
影響有無：
**影響なし（ポジティブな影響あり）**
上記他のバージョンと同様に、このリリースは既存のセキュリティ脆弱性を修正するものであり、機能的な変更や非互換性のある変更は含まれていません。したがって、既存のワークロードや設定への直接的な影響はありません。これらの多数の脆弱性が修正されることにより、Cloud Service Mesh 環境全体のセキュリティが向上します。
対処方法：
Cloud Service Mesh を利用している場合、これらのセキュリティ修正は非常に重要であるため、速やかに本バージョンへのアップグレードを検討することを強く推奨します。アップグレードの際は、公式ドキュメントの手順に従い、テスト環境での動作確認を行ってください。

---

## 用語説明

*   **Cloud Service Mesh (ASM / Anthos Service Mesh):** Google Cloud 上で動作する、Istioベースのマネージドなサービスメッシュプラットフォームです。マイクロサービス間のトラフィック管理、セキュリティポリシーの適用（相互TLSなど）、そして可観測性（メトリクス、ログ、トレース）を提供し、分散システムの運用を容易にします。
*   **Envoy:** Istioを含む多くのサービスメッシュでデータプレーンとして使用される、高性能なオープンソースのL7プロキシです。サイドカーパターンで各アプリケーションのPodにデプロイされ、マイクロサービス間のすべてのネットワークトラフィックをインターセプトして処理します。
*   **CVE (Common Vulnerabilities and Exposures):** 広く知られているソフトウェアのセキュリティ脆弱性に対して一意に割り当てられる識別子です。これにより、脆弱性情報の共有と管理が標準化されます。
*   **GCP-2026-067:** Google Cloudのセキュリティ速報の識別子です。特定のセキュリティ脆弱性に関する公式情報や影響、推奨される対策が記載されています。
*   **In-cluster Cloud Service Mesh:** Cloud Service Mesh のコントロールプレーン（Istiodなど）をユーザーのGKEクラスタ内に直接デプロイし、管理する形態です。これに対し、Google がコントロールプレーンを管理するマネージドコントロールプレーンの形態もあります。
*   **Proxy:** ネットワークトラフィックを中継するサーバー。サービスメッシュの文脈では、通常Envoyプロキシを指し、アプリケーションとネットワークの間でトラフィックのルーティング、ポリシー適用、メトリクス収集などを行います。
*   **Control Plane:** サービスメッシュの管理層。データプレーン（Envoyプロキシなど）に設定やポリシーを配布し、サービスメッシュ全体の動作を制御します。IstioのControl Planeは`Istiod`という単一のバイナリで提供されます。
*   **Distroless:** 必要最小限の実行時依存関係のみを含む軽量なDockerイメージのセットです。OSコンポーネントを極力含まないことで、イメージサイズを削減し、攻撃対象領域を減らしてセキュリティを向上させます。
*   **CNI (Container Network Interface):** Kubernetesクラスタにおいて、コンテナのネットワーク接続を構成するための標準インターフェースです。サービスメッシュでは、CNIプラグインがサイドカープロキシへのトラフィックリダイレクトなどを設定することがあります。
*   **Severity (CVSS Score):** 脆弱性の深刻度を示す指標で、共通脆弱性評価システム（CVSS: Common Vulnerability Scoring System）に基づいたスコアで表現されます。通常は0.0から10.0の範囲で、数値が高いほど深刻度が高いことを示し、High（高）、Medium（中）、Low（低）などのカテゴリに分類されます。