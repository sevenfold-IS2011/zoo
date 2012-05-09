<?xml version="1.0"?>
<xsl:stylesheet
	version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:zoo="http://www.zoo.com">
	<xsl:template match="zoo:workers">
	<html>
		<body>
			<div>
			<h3>Descizione dei dipendenti:</h3>
			<xsl:for-each select="zoo:employee">
				<p>--- Ciao, sono <xsl:value-of select="zoo:name"/>, </p>
				<p>sono un <xsl:value-of select="zoo:gender"/></p>
				<p> e ho <xsl:value-of select="zoo:age"/> anni.</p>
			</xsl:for-each>
			</div>
			<div>
				<h3>Descizione dei manager:</h3>
				<xsl:for-each select="zoo:manager">
					<p>--- Ciao, sono <xsl:value-of select="zoo:name"/>, </p>
					<p>sono un <xsl:value-of select="zoo:gender"/>, </p>
					<p>ho <xsl:value-of select="zoo:age"/> anni e</p>
					<p style="color:red">guadagno <xsl:value-of select="zoo:salary"/> euro.</p>
				</xsl:for-each>
			</div>
		</body>
	</html>
	</xsl:template>
</xsl:stylesheet>

